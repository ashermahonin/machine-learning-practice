"""Задание 4. Сумма отдельных цифр в строке."""

text = input("Введите строку: ")
total = 0

for character in text:
    if character.isdecimal():
        total += int(character)

print(f"Сумма цифр: {total}")
