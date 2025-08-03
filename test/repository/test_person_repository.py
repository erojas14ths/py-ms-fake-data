import unittest

from src.enums.genre_enum import GenreEnum
from src.exceptions.base_generic_exception import FakerUniqueValuesException
from src.repository.person_repository import find_one, find_one_unique, find_all, find_all_unique


class MyTestCase(unittest.TestCase):
    def test_find_one_male(self):
        genre = GenreEnum.male
        result = find_one(genre)
        self.assertEqual(GenreEnum.male.value, result.genre)

    def test_find_one_female(self):
        genre = GenreEnum.female
        result = find_one(genre)
        self.assertEqual(GenreEnum.female.value, result.genre)

    def test_find_one_unique_male(self):
        genre = GenreEnum.male
        result = find_one_unique(genre)
        self.assertEqual(GenreEnum.male.value, result.genre)

    def test_find_one_unique_female(self):
        genre = GenreEnum.female
        result = find_one_unique(genre)
        self.assertEqual(GenreEnum.female.value, result.genre)

    def test_find_all(self):
        size = 10
        genre = GenreEnum.male
        result = find_all(10, genre)
        self.assertEqual(len(result), size)

    def test_find_all_unique(self):
        size = 10
        genre = GenreEnum.male
        result = find_all_unique(10, genre)
        self.assertEqual(len(result), size)

    def test_find_all_unique_error(self):
        result = []
        size = 500
        genre = GenreEnum.male
        try:
            result = find_all_unique(size, genre)
        except FakerUniqueValuesException:
            print(f"Unexpected error was in test")
        self.assertNotEqual(len(result), size)


if __name__ == '__main__':
    unittest.main()
