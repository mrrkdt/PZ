# Сгенерировать словарь вида {0: 1, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36}
# удалив из него второй и третий элементы. отобразить исходный и получившийся словарь.
# использовать for, range.

# -> 7
# <- {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# <- {0: 0, 1: 1, 4: 16, 5: 25}

DICT = {}


def init_dict(m_dict, size):
    # инициализация словаря
    for i in range(size):
        m_dict[i] = i * i


def remove_element_from_dict(m_dict, elements):
    for i in range(len(elements)):
        if elements[i] in m_dict:
            del m_dict[elements[i]]


if __name__ == "__main__":
    size = input("Enter size dict: ")

    # обработка исключений
    while type(size) != int:
        try:
            size = int(size)
        except ValueError:
            size = input("Error. Enter size dict: ")

    init_dict(DICT, size)

    # вывод словаря
    print(f"Before: {DICT}")

    # удаление элементов
    LIST = list(map(int, input("What elements do you want to remove? ").split()))

    remove_element_from_dict(DICT, LIST)

    # вывод словаря
    print(f"After: {DICT}")

