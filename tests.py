from main import BooksCollector

import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать , если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# нельзя добавить одну книгу дважды
    def test_add_new_book_add_one_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 1

# нельзя выставить рейтинг книге, которой нет в списке.
    def test_cant_set_rating_book_not_listed(self):
        collector = BooksCollector()
        collector.set_book_rating('Гордость и предубеждение и зомби', 1)
        assert 'Гордость и предубеждение и зомби' not in collector.books_rating

# Нельзя выставить рейтинг меньше 1.
        def test_cant_set_rating_less_than_one(self):
            collector = BooksCollector()
            collector.add_new_book('Гордость и предубеждение и зомби')
            collector.set_book_rating('Гордость и предубеждение и зомби', 0)
            assert collector.books_rating['Гордость и предубеждение и зомби'] >= 1

# Нельзя выставить рейтинг больше 10.
        def test_cant_set_rating_greater_than_ten(self):
            collector = BooksCollector()
            collector.add_new_book('Гордость и предубеждение и зомби')
            collector.set_book_rating('Гордость и предубеждение и зомби', 11)
            assert collector.books_rating['Гордость и предубеждение и зомби'] <= 10

# У не добавленной книги нет рейтинга.
    def test_set_book_rating_book_not_added_has_no_rating(self):
        collector = BooksCollector()
        collector.set_book_rating('Гордость и предубеждение и зомби' , 1)
        rating = collector.get_book_rating('Гордость и предубеждение и зомби')
        assert rating is None

# Вывод списка книг с определенным рейтингом
    def test_get_books_with_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать , если ваш кот хочет вас убить')
        collector.add_new_book('Python')
        collector.set_book_rating('Python' , 9)
        result = collector.get_books_with_specific_rating(1)
        assert ['Гордость и предубеждение и зомби', 'Что делать , если ваш кот хочет вас убить'] == result

# Нельзя вывести список книг с определенным рейтингом, если нет книг
    def test_get_books_with_specific_rating_fails_if_no_books(self):
        collector = BooksCollector()
        result = collector.get_books_with_specific_rating(1)
        assert [] == result

# Добавление книги в избранное.
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.favorites

# Нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_add_book_in_favorites_not_added_if_not_in_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        del collector.books_rating['Гордость и предубеждение и зомби']
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.favorites

# Проверка удаления книги из избранного.
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.favorites

# Проверка получения списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
