import json
import unittest

from build import render


class RenderTest(unittest.TestCase):
    def test_example_renders_all_sections(self):
        with open("data.example.json", encoding="utf-8") as f:
            page = render(json.load(f))
        for needle in ("Иван Петров", "Python-разработчик", "Telegram Bot API", "Пример-Студия", "https://t.me/example"):
            self.assertIn(needle, page)

    def test_html_is_escaped(self):
        page = render({"name": "<script>alert(1)</script>"})
        self.assertNotIn("<script>alert(1)</script>", page)
        self.assertIn("&lt;script&gt;", page)


if __name__ == "__main__":
    unittest.main()
