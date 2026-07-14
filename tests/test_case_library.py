import hashlib
import importlib.util
import json
import re
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "examples" / "cases" / "dunhuang-museum-hero"


class DunhuangCaseLibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.metadata = json.loads((CASE / "case.json").read_text(encoding="utf-8"))

    def test_archive_contains_only_final_distribution_material(self):
        self.assertEqual(
            {
                "README.md",
                "THIRD_PARTY_NOTICES.md",
                "case.json",
                "licenses",
                "serve.py",
                "site",
            },
            {path.name for path in CASE.iterdir()},
        )
        forbidden_parts = {
            "node_modules",
            "dist",
            "work",
            "screenshots",
            "evidence",
            "qa",
            "src",
        }
        forbidden_names = {
            "package.json",
            "package-lock.json",
            "design-contract.md",
            "design-qa.md",
            "layout-skeleton.html",
            "asset-contract.json",
        }
        for path in CASE.rglob("*"):
            relative = path.relative_to(CASE)
            self.assertTrue(forbidden_parts.isdisjoint(relative.parts), relative)
            self.assertNotIn(path.name.casefold(), forbidden_names, relative)
            if path.is_file() and path.suffix in {".html", ".json", ".md", ".py"}:
                text = path.read_text(encoding="utf-8")
                for machine_path in ("/Users/", "/private/tmp/", "/var/folders/"):
                    self.assertNotIn(machine_path, text, relative)

    def test_case_index_resolves_assets_and_integrity(self):
        self.assertEqual(1, self.metadata["schemaVersion"])
        self.assertEqual("final-implementation-case", self.metadata["kind"])
        self.assertIsNone(self.metadata["formalMaturityClaim"])
        self.assertEqual(
            {"/", "/exhibitions", "/collection", "/digital", "/visit"},
            set(self.metadata["routes"]),
        )
        for asset in self.metadata["assets"]:
            path = CASE / asset["path"]
            self.assertTrue(path.is_file(), asset["path"])
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(asset["sha256"], digest, asset["path"])

    def test_compiled_distribution_has_no_broken_local_references(self):
        site = CASE / "site"
        text_files = [site / "index.html"]
        text_files.extend((site / "assets").glob("*.js"))
        text_files.extend((site / "assets").glob("*.css"))
        bundle_text = "\n".join(path.read_text(encoding="utf-8") for path in text_files)

        absolute_assets = set(re.findall(r"/assets/[A-Za-z0-9._/-]+", bundle_text))
        self.assertTrue(absolute_assets)
        for reference in absolute_assets:
            with self.subTest(reference=reference):
                self.assertTrue((site / reference.lstrip("/")).is_file())

        relative_chunks = set(
            re.findall(r'["\']\./([^"\']+\.(?:js|css))["\']', bundle_text)
        )
        for reference in relative_chunks:
            with self.subTest(reference=reference):
                self.assertTrue((site / "assets" / reference).is_file())

    def test_static_server_serves_every_route_and_rejects_missing_assets(self):
        spec = importlib.util.spec_from_file_location("dunhuang_case_server", CASE / "serve.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.SpaHandler.quiet = True
        server = module.create_server(port=0)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            base = f"http://127.0.0.1:{server.server_address[1]}"
            for route in self.metadata["routes"]:
                with self.subTest(route=route), urllib.request.urlopen(base + route) as response:
                    self.assertEqual(200, response.status)
                    self.assertIn(b'id="root"', response.read())
            asset_request = urllib.request.Request(
                base + "/assets/hero-world.png", method="HEAD"
            )
            with urllib.request.urlopen(asset_request) as response:
                self.assertEqual("image/png", response.headers.get_content_type())
            with self.assertRaises(urllib.error.HTTPError) as missing:
                urllib.request.urlopen(base + "/assets/missing.png")
            self.assertEqual(404, missing.exception.code)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
