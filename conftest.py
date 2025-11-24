import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.books_genre = {
        'Гордость и предубеждение и зомби': 'Ужасы',
        'Что делать, если ваш кот хочет вас убить': 'Мультфильмы',
        'Что делать, если ваш кот убил вас': 'Мультфильмы'
    }
    collector.favorites = ['Что делать, если ваш кот убил вас', 'Что делать, если ваш кот хочет вас убить']
    return collector