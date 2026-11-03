"""Проверка консольных программ: python3 proverka.py."""

from pathlib import Path
import subprocess
import sys
import unittest


DIRECTORY = Path(__file__).resolve().parent


def run_script(filename, values=""):
    result = subprocess.run(
        [sys.executable, str(DIRECTORY / filename)],
        input=values,
        text=True,
        capture_output=True,
        timeout=5,
        check=True,
    )
    return result.stdout


class HomeworkTests(unittest.TestCase):
    def test_sum(self):
        for values, expected in [
            ("10\n-2\n2.5\nстоп\n", "10.5"),
            ("стоп\n", "0"),
            ("1\n2\n\n", "3"),
            (" 2 \n-2\nконец\n999\n", "0"),
            ("1\nnan\n", "1"),
            ("1\ninf\n", "1"),
        ]:
            with self.subTest(values=values):
                output = run_script("summa_chisel.py", values)
                self.assertTrue(output.endswith(f"Сумма: {expected}\n"))

    def test_uppercase(self):
        for text, expected in [("PyThOnПрИвЕт", "PTOПИЕ"), ("python", ""), ("", "")]:
            with self.subTest(text=text):
                output = run_script("zaglavnye_bukvy.py", text + "\n")
                self.assertTrue(output.endswith(f"Заглавные буквы: {expected}\n"))

    def test_fizzbuzz(self):
        lines = run_script("fizzbuzz.py").splitlines()
        self.assertEqual(len(lines), 100)
        self.assertEqual(lines[:5], ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(lines[14], "FizzBuzz")
        self.assertEqual(lines[98:], ["Fizz", "Buzz"])
        self.assertEqual(lines.count("FizzBuzz"), 6)
        self.assertEqual(lines.count("Fizz"), 27)
        self.assertEqual(lines.count("Buzz"), 14)

    def test_digit_sum(self):
        for text, expected in [("a12б3!0", 6), ("нет цифр", 0), ("", 0), ("²٣4", 7)]:
            with self.subTest(text=text):
                output = run_script("summa_cifr.py", text + "\n")
                self.assertTrue(output.endswith(f"Сумма цифр: {expected}\n"))

    def test_maximum(self):
        cases = [
            ("-10\n-9\n-8\n-7\n-6\n-5\n-4\n-3\n-2\n-1\n", "-1"),
            ("7\n" * 10, "7"),
            ("0\n0\n0\n0\n0\n0\n0\n0\n0\n0.5\n", "0.5"),
            ("99\n0\n0\n0\n0\n0\n0\n0\n0\n0\n", "99"),
            ("текст\nnan\ninf\n" + "1\n" * 9 + "2\n1000\n", "2"),
        ]
        for values, expected in cases:
            with self.subTest(values=values):
                output = run_script("maksimum.py", values)
                self.assertTrue(output.endswith(f"Максимум: {expected}\n"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
