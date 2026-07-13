import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "evals" / "source-ledger.json"


class ProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(LEDGER.read_text(encoding="utf-8"))
        cls.sources = {source["id"]: source for source in cls.data["sources"]}

    def test_project_license_is_fixed(self):
        license_record = self.data["projectLicense"]
        self.assertEqual(license_record["id"], "Apache-2.0")
        self.assertEqual(
            license_record["sha256"],
            "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
        )
        self.assertEqual(
            hashlib.sha256((ROOT / license_record["path"]).read_bytes()).hexdigest(),
            license_record["sha256"],
        )

    def test_external_revisions_and_license_hashes_are_fixed(self):
        expected = {
            "taste-skill": (
                "b17742737e796305d829b3ad39eda3add0d79060",
                "4575a543ab88dad12ccea7d97e563d0bce5b448b06072e65d3264497dad326df",
            ),
            "personal-homepage-skill": (
                "e244f4608850e4b38c62d31d89a7181c5beb0e19",
                "2b1c3aff89b56954e91756db3032507ad181d3628ff32f189062c3d7a1f8edf5",
            ),
        }
        self.assertEqual(set(self.sources), set(expected))
        for source_id, (revision, license_hash) in expected.items():
            source = self.sources[source_id]
            self.assertEqual(source["revision"], revision)
            self.assertEqual(len(revision), 40)
            self.assertEqual(source["license"]["sha256"], license_hash)
            self.assertIn(revision, source["license"]["url"])

    def test_current_sources_have_no_reuse_or_dependency(self):
        for source in self.sources.values():
            self.assertEqual(source["accessedAt"], "2026-07-11")
            self.assertTrue(source["reviewedPaths"])
            self.assertTrue(source["reviewPurpose"])
            self.assertTrue(source["independentDerivation"])
            self.assertTrue(source["prohibitedUse"])
            self.assertEqual(source["reuseMode"], "none")
            self.assertEqual(source["materialReused"], [])
            self.assertEqual(source["localDestinations"], [])
            self.assertFalse(source["runtimeDependency"])
            self.assertFalse(source["evaluationDependency"])
            self.assertIsNone(source["noticeArtifact"])
            self.assertIsNone(source["permissionArtifact"])

    def test_restricted_source_is_adoption_blocked(self):
        source = self.sources["personal-homepage-skill"]
        self.assertEqual(source["sourceClass"], "restricted")
        self.assertEqual(source["decision"], "adoption-blocked")

    def test_runtime_has_no_external_source_dependency(self):
        paths = [ROOT / "SKILL.md"] + sorted((ROOT / "references").glob("*.md"))
        text = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        self.assertNotIn("Leonxlnx/taste-skill", text)
        self.assertNotIn("powerycy/personal-homepage-skill", text)

    def test_future_reuse_requires_license_artifacts(self):
        for source in self.sources.values():
            if source["reuseMode"] not in {"adapted", "verbatim"}:
                continue
            self.assertTrue(source["localDestinations"])
            if source["license"]["id"] == "MIT":
                self.assertIsNotNone(source["noticeArtifact"])
                self.assertTrue((ROOT / source["noticeArtifact"]).is_file())
            if source["sourceClass"] == "restricted":
                self.assertIsNotNone(source["permissionArtifact"])
                self.assertTrue((ROOT / source["permissionArtifact"]).is_file())

    def test_static_validation_limit_is_explicit(self):
        self.assertIn("cannot prove absence of copying", self.data["verificationLimit"])


if __name__ == "__main__":
    unittest.main()
