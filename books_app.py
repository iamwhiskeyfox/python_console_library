from DB.adapter import BookDBAdapter
from models import Book

class BooksApp:
    def __init__(self, adapter: BookDBAdapter):
        self.adapter = adapter

    def start(self):
        self.adapter.prepare()
        self._mainloop()

    def _mainloop(self):
        while True:
            command = input('\n Введите команду или напишите help:\n>>> ')
            if command == 'help':
                print('exit - Выйти из команды')
                print('showall - Показать все книги')
                print('add - Добавить команду')
                print('delete - Удалить книгу')
            elif command == 'exit':
                print('Всего хорошего! =)')
                break
            elif command == 'showall':
                books = self.adapter.get_all_books()
                for book in books:
                    print(book)
            elif command == 'add':
                name = input('\n Введите название книги: \n>>>')
                year = int(input('\n Введите год книги: \n>>>'))
                author = input('\n Введите автора книги: \n>>>')
                book = Book(name,year, author, 'Fiction')
                self.adapter.save_new_book(book)
                print('Книга добавлена успешно!')
            elif command == 'delete':
                id = int(input('\n Введите ID книги: \n>>>'))
                book = self.adapter.get_book_by_id(id)
                if book is not None:
                    self.adapter.delete_book(id)
                    print(f'Книга {id} удалена успешно!')
                else:
                    print('Книга не найдена!')
            else:
                print(f"Команда '{command}' не найдена")