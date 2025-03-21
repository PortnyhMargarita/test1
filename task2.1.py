class Книга:
    def __init__(self, id_, название, страницы):
        self.id = id_
        self.название = название
        self.страницы = страницы

    def __str__(self):
        return f'Книга "{self.название}"'

    def __repr__(self):
        return f'Книга (идентификатор={self.id}, название={repr(self.название)}, страницы={self.страницы})'


class Библиотека:
    def __init__(self, книги=None):
        if книги is None:
            self.книги = []
        else:
            self.книги = книги

    def get_next_book_id(self):
        if not self.книги:
            return 1
        return self.книги[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, книга in enumerate(self.книги):
            if книга.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым идентификатором не существует")


# Пример использования
if __name__ == "__main__":
    # Создаем несколько книг
    книга1 = Книга(id_=1, название="1984", страницы=328)
    книга2 = Книга(id_=2, название="О дивный новый мир", страницы=288)

    # Создаем библиотеку и добавляем книги
    библиотека = Библиотека()
    библиотека.книги.append(книга1)
    библиотека.книги.append(книга2)

    # Выводим информацию о книгах
    print(книга1)  # Книга «1984»
    print(книга2)  # Книга «О дивный новый мир»

    # Получаем следующий ID для новой книги
    next_id = библиотека.get_next_book_id()
    print(f"Следующий ID для новой книги: {next_id}")  # Следующий ID для новой книги: 3

    # Получаем индекс книги по ID
    try:
        index = библиотека.get_index_by_book_id(2)
        print(f"Индекс книги с ID 2: {index}")  # Индекс книги с ID 2: 1
    except ValueError as e:
        print(e)

    # Попытка получить индекс несуществующей книги
    try:
        index = библиотека.get_index_by_book_id(99)
    except ValueError as e:
        print(e)  # Книги с запрашиваемым id не существует