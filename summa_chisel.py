"""Задание 1. Сумма чисел до первого нечислового ввода."""

from math import isfinite


total = 0.0

while True:
    value = input("Введите число (любой текст завершит ввод): ")
    try:
        number = float(value)
    except ValueError:
        break

    if not isfinite(number):
        break

    total += number

print(f"Сумма: {total:g}")
