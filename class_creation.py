class Book:
    """
    Класс Book описывает книгу.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Метод __init__ вызывается при создании нового объекта.
        Он задаёт начальное состояние объекта.
        """
        self.title = title
        self.author = author
        self.year = year

    def get_description(self) -> str:
        """
        Метод возвращает текстовое описание книги.
        """
        return f"'{self.title}' — {self.author}, {self.year} год."


book = Book("Преступление и наказание", "Ф. М. Достоевский", 1866)

print(book.get_description())
