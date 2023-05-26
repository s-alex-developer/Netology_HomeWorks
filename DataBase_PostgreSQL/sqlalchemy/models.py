import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

""" Задание 1. СОСТАВИТЬ МОДЕЛИ КЛАССОВ SQLAlchemy ПО СХЕМЕ. """

Base = declarative_base()


class Publisher(Base):

    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.VARCHAR(50), nullable=False)

    # def __str__(self):
    #     return f'{self.id}, {self.name}'


class Book(Base):

    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.VARCHAR(50), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publishers = relationship(Publisher, backref='books')

    # def __str__(self):
    #     return f'{self.id}, {self.title}, {self.id_publisher}'


class Shop(Base):

    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.VARCHAR(50), nullable=False)

    # def __str__(self):
    #     return f"{self.id}, {self.name}"


class Stock(Base):

    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    books = relationship(Book, backref='stocks')
    shops = relationship(Shop, backref='stocks')

    # def __str__(self):
    #     return f"{self.id}, {self.id_book}, {self.id_shop}, {self.count}"


class Sale(Base):

    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.NUMERIC, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stocks = relationship(Stock, backref='sales')

    # def __str__(self):
    #     return f"{self.id}, {self.price}, {self.date_sale}, {self.id_stock}, {self.count}"


def delete_tables(engine):

    Base.metadata.drop_all(engine)


def create_tables(engine):

    Base.metadata.create_all(engine)
