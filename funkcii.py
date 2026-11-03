"""Домашняя работа 3. Функции, аргументы и обработка ввода."""


def calculate(*numbers, operation):
    """Выполнить sum (сложение) или mul (умножение) для всех чисел."""
    if operation == "sum":
        result = 0
        for number in numbers:
            result += number
    elif operation == "mul":
        result = 1
        for number in numbers:
            result *= number
    else:
        raise ValueError("Неизвестная операция. Используйте 'sum' или 'mul'.")

    return result


def read_int(prompt="Введите целое число: "):
    """Запрашивать значение, пока пользователь не введёт целое число."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def full_path(drive, *parts, ext, sep="/"):
    """Собрать путь из диска, папок и имени файла без расширения."""
    if not parts:
        raise ValueError("Укажите имя файла после названия диска.")
    if not sep:
        raise ValueError("Разделитель не должен быть пустым.")

    path = sep.join((drive, *parts))
    if ext:
        path += "." + ext.removeprefix(".")

    return path


def group_by_type(items):
    """Сгруппировать объекты по их точному типу, сохранив порядок."""
    groups = {}

    for item in items:
        item_type = type(item)
        if item_type not in groups:
            groups[item_type] = []
        groups[item_type].append(item)

    return groups


def main():
    print("1. Операции над числами")
    print("Сумма:", calculate(2, 3, 4, operation="sum"))
    print("Произведение:", calculate(2, 3, 4, operation="mul"))

    print("\n2. Ввод целого числа")
    number = read_int()
    print("Введено:", number)

    print("\n3. Путь к файлу")
    print(full_path("c:", "work", "python", "function", "main", ext="py"))

    print("\n4. Группировка по типам")
    items = [1, "python", 2.5, True, 2, "курс", None, [1, 2], {"a": 1}]
    print(group_by_type(items))


if __name__ == "__main__":
    main()
