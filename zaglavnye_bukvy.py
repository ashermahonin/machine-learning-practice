"""Задание 2. Выбор букв в верхнем регистре."""

text = input("Введите строку: ")
result = ""

for character in text:
    if character.isupper():
        result += character

print(f"Заглавные буквы: {result}")
