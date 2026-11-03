"""Задание 5. Максимум из десяти введённых чисел."""

from math import isfinite


maximum = None

for index in range(1, 11):
    while True:
        value = input(f"Введите число {index} из 10: ")
        try:
            number = float(value)
        except ValueError:
            print("Ошибка: введите число.")
            continue

        if not isfinite(number):
            print("Ошибка: введите конечное число.")
            continue

        break

    if maximum is None or number > maximum:
        maximum = number

print(f"Максимум: {maximum:g}")
