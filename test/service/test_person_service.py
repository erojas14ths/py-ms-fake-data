import unittest

from src.enums.genre_enum import GenreEnum
from src.service.person_service import find_one, find_all


class MyTestCase(unittest.TestCase):
    def test_find_one(self):
        genre = GenreEnum.male
        result = find_one(genre)
        self.assertIsNotNone(result.id)

    def test_find_all(self):
        size = 500
        unique = False
        genre = GenreEnum.male
        result = find_all(size, unique, genre)
        self.assertEqual(len(result), size)
    def test_find_all_unique(self):
        size = 500
        unique = True
        genre = GenreEnum.male
        result = find_all(size, unique, genre)
        self.assertNotEqual(len(result), size)

if __name__ == '__main__':
    unittest.main()
