import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "scripts" / "design_layer_tool.py"


def sample_document():
    return {
        "version": "0.1",
        "canvas": {
            "width": 1600,
            "height": 1000,
            "background": "#eef4ff",
        },
        "theme": {
            "fontFamily": "Inter, Arial, sans-serif",
            "colors": {
                "ink": "#10223f",
                "surface": "#ffffff",
                "accent": "#2f6df6",
                "amber": "#d69a27",
            },
        },
        "pages": [
            {
                "id": "home",
                "name": "Homepage",
                "layers": [
                    {
                        "id": "hero-title",
                        "type": "text",
                        "role": "headline",
                        "text": "Launch certainty",
                        "x": 120,
                        "y": 180,
                        "width": 520,
                        "height": 92,
                        "style": {
                            "fontSize": 52,
                            "fontWeight": 700,
                            "color": "#10223f",
                        },
                    },
                    {
                        "id": "cta",
                        "type": "shape",
                        "role": "primary-action",
                        "shape": "roundRect",
                        "x": 120,
                        "y": 340,
                        "width": 190,
                        "height": 56,
                        "style": {
                            "fill": "#2f6df6",
                            "radius": 18,
                        },
                    },
                    {
                        "id": "proof-chart",
                        "type": "chart",
                        "role": "proof",
                        "chart": "bar",
                        "x": 900,
                        "y": 250,
                        "width": 420,
                        "height": 260,
                        "data": [
                            {"label": "Draft", "value": 32},
                            {"label": "Reviewed", "value": 68},
                            {"label": "Approved", "value": 92},
                        ],
                        "style": {
                            "fill": "#2f6df6",
                            "axis": "#7890b3",
                            "text": "#10223f",
                        },
                    },
                ],
            }
        ],
    }


class DesignLayerToolTest(unittest.TestCase):
    def run_tool(self, *args, cwd=None):
        return subprocess.run(
            [sys.executable, str(TOOL), *args],
            cwd=cwd or ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_validates_and_exports_html(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            doc_path = tmp_path / "sample.layerdoc.json"
            html_path = tmp_path / "out" / "sample.html"
            doc_path.write_text(json.dumps(sample_document()), encoding="utf-8")

            validate = self.run_tool("validate", str(doc_path))
            self.assertEqual(validate.returncode, 0, validate.stderr)
            self.assertIn("valid", validate.stdout.lower())

            html = self.run_tool("html", str(doc_path), str(html_path))
            self.assertEqual(html.returncode, 0, html.stderr)
            html_text = html_path.read_text(encoding="utf-8")
            self.assertIn('data-layer-id="hero-title"', html_text)
            self.assertIn("Launch certainty", html_text)
            self.assertIn('data-layer-id="proof-chart"', html_text)

    def test_rejects_unknown_layer_type(self):
        doc = sample_document()
        doc["pages"][0]["layers"].append(
            {
                "id": "bad-layer",
                "type": "unknown",
                "x": 0,
                "y": 0,
                "width": 10,
                "height": 10,
            }
        )
        with tempfile.TemporaryDirectory() as tmp:
            doc_path = Path(tmp) / "bad.layerdoc.json"
            doc_path.write_text(json.dumps(doc), encoding="utf-8")

            validate = self.run_tool("validate", str(doc_path))
            self.assertNotEqual(validate.returncode, 0)
            self.assertIn("unknown layer type", validate.stderr.lower())


if __name__ == "__main__":
    unittest.main()
