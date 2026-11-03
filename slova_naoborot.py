"""Задание 2. Обратный порядок слов."""

text = input("Введите строку: ")
words = text.split()
words.reverse()
result = " ".join(words)

print(result)
