import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book('Гарри Поттер и Философский камень')
        collector.add_new_book('Гарри Поттер и Тайная комната')

        assert len(collector.books_genre) == 2
        
    def test_add_new_book_does_not_add_duplicate(self, collector):

        collector.add_new_book('Гарри Поттер и Тайная комната')
        collector.add_new_book('Гарри Поттер и Тайная комната')

        assert len(collector.books_genre) == 1
        assert collector.books_genre['Гарри Поттер и Тайная комната'] == ''

    def test_add_new_book_check_length_is_not_over_limit(self, collector):

        name = 'A'* 41

        collector.add_new_book(name)

        assert len(collector.books_genre) == 0


    def test_set_book_genre_sets_genre_for_existing_book(self, book):
        book_name = 'Гарри Поттер и Философский камень'

        book.set_book_genre(book_name, 'Фантастика')

        assert book.books_genre[book_name] == 'Фантастика'

    def test_set_book_genre_with_invalid_genre(self, book):

        book_name = 'Гарри Поттер и Философский камень'

        book.set_book_genre(book_name, 'Драма')

        assert book.books_genre[book_name] == ''
     

    def test_get_book_genre_returns_correct_genre(self, genres):

        book_name = 'Гарри Поттер и Философский камень'
        expected_genre = 'Фантастика'

        result =  genres.get_book_genre(book_name)
        assert result == expected_genre

    def test_get_book_genre_for_book_without_genre_returns_empty_string(self, book):
        book_name = 'Гарри Поттер и Философский камень'

        assert book.get_book_genre(book_name) == ''    

    @pytest.mark.parametrize('expected_genre, expected_books',
                            [ 
                                ('Фантастика', ['Гарри Поттер и Философский камень']),
                                ('Ужасы', ['Оно']),
                                ('Детективы', ['Шерлок Холмс'])
                            ]     
                            )
    def test_books_with_specific_genre_return_correct_books(self, genres, expected_genre, expected_books):

        result = genres.get_books_with_specific_genre(expected_genre)
        assert result == expected_books

    def test_get_books_genre_return_correct_dictionary(self, genres):
        expected = {
            'Гарри Поттер и Философский камень': 'Фантастика',
            'Оно': 'Ужасы',
            'Шерлок Холмс': 'Детективы'
        }
        
        result = genres.get_books_genre()

        assert result == expected

    def test_get_books_for_children_return_only_allowed_books(self, genres):
        result = genres.get_books_for_children()
        
        assert 'Гарри Поттер и Философский камень' in result
        assert 'Оно' not in result
        assert 'Шерлок Холмс' not in result

    def test_add_book_in_favorites_add_one_book(self, book):
        book_name = 'Гарри Поттер и Философский камень'

        book.add_book_in_favorites(book_name)

        assert book_name in book.get_list_of_favorites_books()

    def test_delete_book_in_favourites(self, book):
        book_name = 'Гарри Поттер и Философский камень'

        book.add_book_in_favorites(book_name)
        book.delete_book_from_favorites(book_name)

        assert book_name not in book.get_list_of_favorites_books()

    def test_get_list_of_favorites_returns_correct_list(self, book):
         book.add_book_in_favorites('Гарри Поттер и Философский камень')  
         book.add_book_in_favorites('Тесс из рода Дэрбервиллей')   

         favorites = book.get_list_of_favorites_books()

         assert favorites == ['Гарри Поттер и Философский камень', 'Тесс из рода Дэрбервиллей']        

