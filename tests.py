from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_successful_add_two_books(self, collector):
        collector.add_new_book('Гордость и зомби')
        collector.add_new_book('Что делать, если ты кот')
        assert len(collector.books_genre) == 5

    def test_add_new_book_unsuccessful_add_long_name_books(self, collector):
        #Проверка на добавление элемента с более чем 41 символом
        collector.add_new_book('Что делать, если ты котttttttttttttttttttttttttttttttttttttttttttttttttttt')
        assert len(collector.books_genre) == 3

    def test_add_new_book_unsuccessful_add_empty_name_books(self, collector):
        #Проверка на добавление элемента пустым названием
        collector.add_new_book('')
        assert len(collector.books_genre) == 3

    def test_set_book_genre_successful_add_book(self, collector):
        #Проверка что к существующей книге добавится или изменится жанр
        collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Фантастика'

    def test_set_book_genre_unsuccessful_set_book_genre(self, collector):
        #Проверка что жанр не добавится так как жанр написан с ошибкой
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Детектив')
        assert collector.books_genre['Что делать, если ваш кот хочет вас убить'] != 'Детектив'

    def test_set_book_genre_second_unsuccessful_set_book_genre(self, collector):
        #Проверка что жанр не изменится так как книги не существует
        collector.set_book_genre('Что делать, если ваш кот убил вассс','Детективы')
        assert 'Что делать, если ваш кот убил васcc' not in collector.books_genre

    def test_get_book_genre_get_three_genre(self, collector):
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_successful_get_names_with_only_one_genre(self, collector):
        assert collector.get_books_with_specific_genre('Мультфильмы') == \
        ['Что делать, если ваш кот хочет вас убить', 'Что делать, если ваш кот убил вас']

    def test_get_books_with_specific_genre_unsuccessful_get_name_with_not_existed_genre(self, collector):
        #Проверка на сортировку с несуществующим жанром в списке(вторая проверка)
        assert collector.get_books_with_specific_genre('Драммы') == [] 
    
    def test_get_books_with_specific_genre_unsuccessful_get_names_with_not_existed_book(self, collector):
        #Проверка на сортировку с существующим жанром, но с несуществуюший книги в библиотеке(третья проверка)
        assert collector.get_books_with_specific_genre('Детективы') == [] 

    def test_get_books_genre_get_books_genre(self, collector):
        assert collector.get_books_genre() == {
        'Гордость и предубеждение и зомби':'Ужасы',
        'Что делать, если ваш кот хочет вас убить':'Мультфильмы',
        'Что делать, если ваш кот убил вас': 'Мультфильмы'
        }
    
    def test_get_books_for_children_get_books_without_genre_age_rating(self, collector):
        assert collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить', 'Что делать, если ваш кот убил вас']
    
    def test_add_book_in_favorites_successful_add_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == [
            'Что делать, если ваш кот убил вас',
            'Что делать, если ваш кот хочет вас убить',
            'Гордость и предубеждение и зомби'
            ]
        
    def test_add_book_in_favorites_unsuccessful_add_not_existed_book_in_favorites(self, collector):
        #Проверка на добавление несуществующего элемента
        collector.add_book_in_favorites('Что делать, если ваш кот убил ваccc')
        assert collector.favorites == [
            'Что делать, если ваш кот убил вас',
            'Что делать, если ваш кот хочет вас убить'
            ]
        
    def test_add_book_in_favorites_unsuccessful_add_copy_book_in_favorites(self, collector):
        #Проверка на добавление копии элемента
        collector.add_book_in_favorites('Что делать, если ваш кот убил вас')
        assert collector.favorites == [
            'Что делать, если ваш кот убил вас',
            'Что делать, если ваш кот хочет вас убить'
            ]

    def test_delete_book_from_favorites_successful_delete_book_from_favorites(self, collector):
        collector.delete_book_from_favorites('Что делать, если ваш кот убил вас')
        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_unsuccessful_delete_book_from_favorites(self, collector):
        #Проверак на удаление несуществующего элемента
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Что делать, если ваш кот убил вас', 'Что делать, если ваш кот хочет вас убить']

    def test_get_list_of_favorites_books_get_list_of_favorites_books(self, collector):
        assert collector.get_list_of_favorites_books() == [
            'Что делать, если ваш кот убил вас',
            'Что делать, если ваш кот хочет вас убить'
            ]
           