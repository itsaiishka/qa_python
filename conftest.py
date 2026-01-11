import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def book():
    collector = BooksCollector()

    books = ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить', 'Тесс из рода Дэрбервиллей', 'Гарри Поттер и Философский камень']
    for book_name in books:
        collector.add_new_book(book_name)
    return collector

@pytest.fixture
def genres():
    collector = BooksCollector()

    collector.add_new_book('Гарри Поттер и Философский камень')
    collector.add_new_book('Оно')
    collector.add_new_book('Шерлок Холмс')
    
    collector.set_book_genre('Гарри Поттер и Философский камень', 'Фантастика')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')
    return collector
        