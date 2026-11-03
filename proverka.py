"""Проверка программ: python3 proverka.py."""

from ast import literal_eval
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
import subprocess
import sys
import unittest


DIRECTORY = Path(__file__).resolve().parent


def run_script(filename, text):
    result = subprocess.run(
        [sys.executable, str(DIRECTORY / filename)],
        input=text + "\n",
        text=True,
        capture_output=True,
        timeout=5,
        check=True,
    )
    return result.stdout.removeprefix("Введите строку: ").rstrip("\n")


class HomeworkTests(unittest.TestCase):
    def test_character_counts(self):
        cases = [("Aa а!а", {"A": 1, "a": 1, " ": 1, "а": 2, "!": 1}), ("", {})]
        for text, expected in cases:
            with self.subTest(text=text):
                output = run_script("chastota_simvolov.py", text)
                self.assertEqual(literal_eval(output), expected)

    def test_reverse_words(self):
        cases = [
            ("Python is really cool", "cool really is Python"),
            ("  Привет,   мир!  ", "мир! Привет,"),
            ("одно", "одно"),
            ("", ""),
            ("   ", ""),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(run_script("slova_naoborot.py", text), expected)

    def test_remove_duplicates(self):
        with redirect_stdout(StringIO()):
            values = runpy.run_path(str(DIRECTORY / "bez_dublikatov.py"))
        self.assertEqual(values["result"], [1, "python", [2, 3], {"a": 1}, 4])
        self.assertEqual(
            values["items"],
            [1, "python", 1, [2, 3], "python", {"a": 1}, [2, 3], {"a": 1}, 4],
        )

    def test_unique_elements(self):
        with redirect_stdout(StringIO()):
            values = runpy.run_path(str(DIRECTORY / "unikalnye_elementy.py"))
        self.assertEqual(values["result"], [1, 2, [3], "python", {"a": 1}, 4])
        self.assertEqual(values["first"], [1, 2, [3]])
        self.assertEqual(values["second"], [2, "python", [3]])
        self.assertEqual(values["third"], ["python", {"a": 1}, 4])

    def test_character_categories(self):
        cases = [
            ("Привет, Python! 123", (3, 9, 3, 2)),
            ("Ёж, Ау! «Да»…", (4, 2, 0, 5)),
            ("ьъЬЪ \t$+🙂²", (0, 0, 0, 0)),
            ("٣4", (0, 0, 2, 0)),
            ("", (0, 0, 0, 0)),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                result = literal_eval(run_script("tipy_simvolov.py", text))
                self.assertEqual(
                    result,
                    dict(zip(("гласные", "согласные", "цифры", "пунктуация"), expected)),
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
