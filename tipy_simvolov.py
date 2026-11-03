"""Задание 5. Подсчёт букв, цифр и знаков пунктуации."""

from unicodedata import category


text = input("Введите строку: ")
vowels = "aeiouаеёиоуыэюя"
consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
counts = {"гласные": 0, "согласные": 0, "цифры": 0, "пунктуация": 0}

for character in text:
    letter = character.lower()
    if letter in vowels:
        counts["гласные"] += 1
    elif letter in consonants:
        counts["согласные"] += 1
    elif character.isdecimal():
        counts["цифры"] += 1
    elif category(character).startswith("P"):
        counts["пунктуация"] += 1

print(counts)
