class READER:
    def __init__(self, name, number, date_of_birth):
        self.name = name
        self.number = number
        self.date_of_birth = date_of_birth
        self.read_books = []
        self.current_books = []

    def add_book(self, book):
        """Отримання книги на руки"""
        self.current_books.append(book)

    def return_book(self, book):
        """Повернення книги в бібліотеку"""
        if book in self.current_books:
            self.current_books.remove(book)
            self.read_books.append(book)
        else:
            print(f"Книга '{book}' не знайдена у списку поточних книг")

    def show_current_books(self):
        """Виведення на екран списку поточних книг"""
        print("Поточні книги:", self.current_books)

    def show_read_books(self):
        """Виведення на екран списку прочитаних книг"""
        print("Прочитані книги:", self.read_books)

reader1 = READER("Іванов Іван Іванович", 123, "01.01.1980")
reader2 = READER("Петренко Петро Петрович", 124, "02.02.1990")
reader3 = READER("Сидоренко Сидір Сидорович", 125, "03.03.2000")

reader1.add_book("Гаррі Поттер і філософський камінь")
reader1.add_book("Володар перснів: Хранителі Персня")
reader2.add_book("Місто сонця")
reader3.add_book("Код да Вінчі")

reader1.return_book("Гаррі Поттер і філософський камінь")

print(f"Читач: {reader1.name}")
reader1.show_current_books()
reader1.show_read_books()

print(f"\nЧитач: {reader2.name}")
reader2.show_current_books()
reader2.show_read_books()

print(f"\nЧитач: {reader3.name}")
reader3.show_current_books()
reader3.show_read_books()
