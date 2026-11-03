"""Задание 3. Удаление дубликатов с сохранением порядка."""

items = [1, "python", 1, [2, 3], "python", {"a": 1}, [2, 3], {"a": 1}, 4]
result = []

for item in items:
    if item not in result:
        result.append(item)

print(result)
