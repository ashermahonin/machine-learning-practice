"""Задание 4. Уникальные элементы нескольких списков."""

first = [1, 2, [3]]
second = [2, "python", [3]]
third = ["python", {"a": 1}, 4]
lists = [first, second, third]
result = []

for items in lists:
    for item in items:
        if item not in result:
            result.append(item)

print(result)
