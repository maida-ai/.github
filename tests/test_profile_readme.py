"""The organization profile teaches the released own-repository route."""

from pathlib import Path
import re
import unittest


class ProfileReadmeTests(unittest.TestCase):
    def test_first_report_and_next_change(self):
        text = (Path(__file__).resolve().parents[1] / "profile/README.md").read_text()
        block = text.split("```bash\n", 1)[1].split("```", 1)[0]
        self.assertIn('uv tool install "maida-ai==0.6.1"', block)
        self.assertIn("cd my-repo", block)
        self.assertLess(block.index("maida init"), block.index("maida check"))
        self.assertLess(block.index("maida check"), block.index('exact "View:" command'))
        self.assertIn("maida view 83aa19e3", text)
        for example in re.findall(r"```bash\n(.*?)```", text, re.S):
            self.assertNotRegex(example, r"<[A-Z][A-Z_]*>")
        self.assertIn("Claude Code task", block)
        self.assertIn("3 active checks passed", text)
        self.assertIn("## Protect the next agent change", text)
        self.assertIn("$15", text)
        self.assertIn("VIP", text)
        self.assertEqual(set(re.findall(r"Maida (?:v)?(\d+\.\d+\.\d+)", text)), {"0.6.1"})
        self.assertEqual(set(re.findall(r"maida-ai==([\d.]+)", text)), {"0.6.1"})
        self.assertNotRegex(text, r"maida-ai/maida-assert@(?:V\d|v\d)")
        self.assertLess(text[: text.index("```bash")].count("\n"), 40)
        for obsolete in ("unreleased", "MAIDA_DATA_DIR", "install_capture", "--expect-status", "@v5", "@V4"):
            self.assertNotIn(obsolete, text)
