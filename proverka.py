"""Проверка функций: python3 proverka.py."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from funkcii import calculate, full_path, group_by_type, read_int


class HomeworkTests(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate(2, 3, 4, operation="sum"), 9)
        self.assertEqual(calculate(2, 3, 4, operation="mul"), 24)
        self.assertEqual(calculate(-2, 0.5, operation="sum"), -1.5)
        self.assertEqual(calculate(-2, 0.5, operation="mul"), -1)
        self.assertEqual(calculate(3, 0, -2, operation="mul"), 0)

    def test_empty_calculation(self):
        self.assertEqual(calculate(operation="sum"), 0)
        self.assertEqual(calculate(operation="mul"), 1)

    def test_unknown_operation(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, operation="divide")
        with self.assertRaises(TypeError):
            calculate(1, 2, "sum")

    def test_integer_retry(self):
        with patch("builtins.input", side_effect=["abc", "2.5", "", " -7 "]):
            with redirect_stdout(StringIO()) as output:
                self.assertEqual(read_int(), -7)
        self.assertEqual(output.getvalue().count("Ошибка: введите целое число."), 3)

    def test_integer_zero(self):
        with patch("builtins.input", return_value="+0"):
            self.assertEqual(read_int(), 0)

    def test_full_path(self):
        self.assertEqual(
            full_path("c:", "work", "python", "function", "main", ext="py"),
            "c:/work/python/function/main.py",
        )
        self.assertEqual(full_path("c:", "main", ext="py"), "c:/main.py")
        self.assertEqual(full_path("d:", "данные", "отчёт", ext=".txt"), "d:/данные/отчёт.txt")
        self.assertEqual(full_path("c:", "main", ext=""), "c:/main")
        self.assertEqual(
            full_path("c:", "work", "main", ext="py", sep="\\"),
            "c:\\work\\main.py",
        )

    def test_invalid_path(self):
        with self.assertRaises(ValueError):
            full_path("c:", ext="py")
        with self.assertRaises(ValueError):
            full_path("c:", "main", ext="py", sep="")

    def test_group_by_type(self):
        nested_list = [1, 2]
        nested_dict = {"a": 1}
        items = [1, "a", 2.5, True, 2, "b", None, nested_list, nested_dict, False]
        original = items.copy()
        self.assertEqual(
            group_by_type(items),
            {
                int: [1, 2],
                str: ["a", "b"],
                float: [2.5],
                bool: [True, False],
                type(None): [None],
                list: [nested_list],
                dict: [nested_dict],
            },
        )
        self.assertEqual(items, original)
        self.assertEqual(group_by_type([]), {})

    def test_console_program(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("funkcii.py"))],
            input="ошибка\n42\n",
            text=True,
            capture_output=True,
            timeout=5,
            check=True,
        )
        for expected in [
            "Сумма: 9",
            "Произведение: 24",
            "Введено: 42",
            "c:/work/python/function/main.py",
            "<class 'bool'>: [True]",
        ]:
            with self.subTest(expected=expected):
                self.assertIn(expected, result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
