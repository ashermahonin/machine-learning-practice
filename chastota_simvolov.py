"""Задание 1. Количество вхождений каждого символа."""

text = input("Введите строку: ")
counts = {}

for character in text:
    counts[character] = counts.get(character, 0) + 1

print(counts)
