from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и зомби')
        collector.add_new_book('Что делать, если ты кот')
        #Проверка на добавление элемента с более чем 41 символом
        collector.add_new_book('Что делать, если ты котttttttttttttttttttttttttttttttttttttttttttttttttttt')
        #Проверка на добавление элемента пустым названием
        collector.add_new_book('')
        assert len(collector.books_genre) == 5

    def test_set_book_genre_add_three_books(self, collector):
        #Проверка что к существующей книге добавится или изменится жанр
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        #Проверка что жанр не добавится так как жанр написан с ошибкой
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Детектив')
        #Проверка что жанр не изменится так как книги не существует
        collector.set_book_genre('Что делать, если ваш кот убил вассс','Детективы')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Фантастика' and \
        collector.books_genre['Что делать, если ваш кот хочет вас убить'] != 'Детектив' and \
        'Что делать, если ваш кот убил васcc' not in collector.books_genre

    def test_get_book_genre_get_three_genre(self, collector):
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы' and \
        collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Мультфильмы'

    def test_get_books_with_specific_genre_get_names_with_only_one_genre(self, collector):
        #Проверка на сортировку с несуществующим жанром в списке(вторая проверка)
        #Проверка на сортировку с существующим жанром, но с несуществуюший книги в библиотеке(третья проверка)
        assert collector.get_books_with_specific_genre('Мультфильмы') == \
        ['Что делать, если ваш кот хочет вас убить', 'Что делать, если ваш кот убил вас'] and\
        collector.get_books_with_specific_genre('Драммы') == [] and\
        collector.get_books_with_specific_genre('Детективы') == [] 

    def test_get_books_genre_get_books_genre(self, collector):
        assert collector.get_books_genre() == {
        'Гордость и предубеждение и зомби':'Ужасы',
        'Что делать, если ваш кот хочет вас убить':'Мультфильмы',
        'Что делать, если ваш кот убил вас': 'Мультфильмы'
        }
    
    def test_get_books_for_children_get_books_without_genre_age_rating(self, collector):
        assert collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить', 'Что делать, если ваш кот убил вас']
    
    def test_add_book_in_favorites_get_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        #Проверак на добавление несуществующего элемента
        collector.add_book_in_favorites('Что делать, если ваш кот убил ваccc')
        #Проверка на добавление копии элемента
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == [
            'Что делать, если ваш кот убил вас',
            'Что делать, если ваш кот хочет вас убить',
            'Гордость и предубеждение и зомби'
            ]

    def test_delete_book_from_favorites_get_favorites_without_book(self, collector):
        collector.delete_book_from_favorites('Что делать, если ваш кот убил вас')
        #Проверак на удаление несуществующего элемента
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить']

    def test_get_list_of_favorites_books_get_list_of_favorites_books(self, collector):
        assert collector.get_list_of_favorites_books() == [
            'Что делать, если ваш кот убил вас',
            'Что делать, если ваш кот хочет вас убить'
            ]
           