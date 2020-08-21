from peewee import *
from datetime import datetime
import random

journal = []
db = SqliteDatabase("books1.db")


# db = PostgresqlDatabase("books.db")
# db = MySQLDatabase("books.db")


class Book(Model):
    name = CharField(max_length=100, verbose_name="Название")
    year = IntegerField(verbose_name="Год")
    created_at = DateTimeField(verbose_name="Дата создания")
    genre = CharField(max_length=20, verbose_name="Жанр")

    class Meta:
        database = db


class Sale(Model):
    price = FloatField(verbose_name="Цена одной книги")
    count = IntegerField(verbose_name="Кол-во", default=1)
    book = ForeignKeyField(Book, verbose_name="Книга", backref="sales")
    transaction_date = DateTimeField(verbose_name="Время продажи")

    class Meta:
        database = db


db.connect()

db.create_tables([Book, Sale])

# book = Book(name="Жамиля", year=1970, created_at=datetime.now(), genre="драма")
# book.save()
#
# Book.create(name="Пегий пес", year=1979, created_at=datetime.now(), genre="драма")
# Book.create(name="Манкурт", year=1999, created_at=datetime.now(), genre="драма")

# for book in Book.select().execute():
#     for i in range(random.randint(1, 5)):
#         Sale.create(price=random.randint(100, 1000), count=1, book=book,
#                     transaction_date=datetime(2020, 7, random.randint(1, 30)))


# for book in Book.select():
#     count = (Sale.select().where(Sale.book == book)).count()
#     print('\t', book.name, '\t', count)

# Вытащить общую сумму продаж для каждой книги и колво
books = Book.select(Book, fn.Count(Sale.id).alias("sales_count"), fn.Sum(Sale.price).alias('sales_sum')).join(
    Sale).group_by(Sale.book)
for book in books:
    print('\t', book.name, '\t', book.sales_count, '\t', book.sales_sum)

# sales = Sale.select(Sale,Book).join(Book).order_by(Sale.transaction_date)
# for sale in sales:
#     print('\t', sale.book.name, '\t', sale.price, '\t', sale.count, '\t', sale.transaction_date, '\t')

# sales = Sale.select(Sale,Book).join(Book).count()
# sale_count = Sale.select().count()
# for sale in sales:
#     print('\t', sale.book.name, '\t',sale_count)
