class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "Прочитана" if self.read else "Непрочитана"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("библиотека пуста")
        for book in self.books:
            print(book)

    def find_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        return found_books

    def find_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        return found_books

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                print(f"книга '{title}' отмечена как прочитанная")
                return
        print(f"книга '{title}' не найдена")

    def mark_book_as_unread(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_unread()
                print(f"книга '{title}' отмечена как непрочитанная")
                return
        print(f"книга '{title}' не найдена")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"книга '{title}' удалена из библиотеки")
                return
        print(f"книга '{title}' не найдена")

    def filter_by_status(self, read_status):
        filtered_books = [book for book in self.books if book.read == read_status]
        if not filtered_books:
            print("Нет книг с таким статусом.")
        for book in filtered_books:
            print(book)


def main():
    library = Library()

    while True:
        print("Доступные команды:")
        print("1. Добавить книгу")
        print("2. Просмотреть список книг")
        print("3. Найти книгу по названию")
        print("4. Найти книги по автору")
        print("5. Отметить книгу как прочитанную")
        print("6. Отметить книгу как непрочитанную")
        print("7. Удалить книгу")
        print("8. Фильтровать книги по статусу")
        print("0. Выход")
        
        choice = input("Выберите команду: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год публикации: ")
            library.add_book(Book(title, author, year))
            print("Книга добавлена.")

        elif choice == '2':
            library.list_books()

        elif choice == '3':
            title = input("Введите название книги для поиска: ")
            books = library.find_by_title(title)
            for book in books:
                print(book)
            if not books:
                print("Книга не найдена.")

        elif choice == '4':
            author = input("Введите автора для поиска: ")
            books = library.find_by_author(author)
            for book in books:
                print(book)
            if not books:
                print("Книги не найдены.")

        elif choice == '5':
            title = input("Введите название книги, которую хотите отметить как прочитанную: ")
            library.mark_book_as_read(title)

        elif choice == '6':
            title = input("Введите название книги, которую хотите отметить как непрочитанную: ")
            library.mark_book_as_unread(title)

        elif choice == '7':
            title = input("Введите название книги, которую хотите удалить: ")
            library.remove_book(title)

        elif choice == '8':
            status = input("Введите статус : ")
            if status == "прочитанные":
                library.filter_by_status(True)
            elif status == "непрочитанные":
                library.filter_by_status(False)
            else:
                print("Неверный статус.")

        elif choice == '0':
            print("Выход из программы.")
            break

        else:
            print("Неверная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
