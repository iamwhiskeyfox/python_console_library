class Book:
    def __init__(self, name, year, author, genre):
        self.id = 0
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f'{self.id}. {self.name}, {self.year}, {self.author}, {self.genre}'
