import pickle


# Блок 1

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.content = ""

    def read(self):
        return self.content

    def write(self, text):
        self.content += text


# Пример использования
book1 = Book("Программирование по Python", "Guido van Rossum", 400)
book1.write("Chapter 1: Ознакомление с Python\n")
book1.write("Chapter 2: Переменные и типы данных\n")

print("Название книги:", book1.title)
print("Автор книги:", book1.author)
print("Количество страниц:", book1.num_pages, end="\n\n")
print("Содержание:")
print(book1.read())

print("\n")

# Блок 2


class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Apple(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color


class Orange(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color


# Пример использования
apple = Apple("Яблоко", 150, "Красный")
orange = Orange("Апельсин", 200, "Оранжевый")

print("Название яблока:", apple.name)
print(f"Вес яблока: {apple.weight} грамм")
print("Цвет яблока:", apple.color)

print("Название апельсина:", orange.name)
print(f"Вес апельсина: {orange.weight} грамм")
print("Цвет апельсина:", orange.color)

print("\n")


# Блок 3

def save_def(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)


def load_def(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


# Пример использования
book2 = Book("Машинное обучение", "Andrew Ng", 300)
save_def(book2, "book2.pkl")

loaded_book = load_def("book2.pkl")

print("Название загруженной книги:", loaded_book.title)
print("Автор загруженной книги:", loaded_book.author)
print("Количество страниц загруженной книги:", loaded_book.num_pages)
