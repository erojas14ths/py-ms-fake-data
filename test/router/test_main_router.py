import unittest

from fastapi.testclient import TestClient

from main import app
from src.constants.fake_constants import GENRE_MALE
from src.enums.genre_enum import GenreEnum

client = TestClient(app)


class MyTestCase(unittest.TestCase):
    def test_router_find_one(self):
        genre = GenreEnum.male
        response = client.get("/person", params={"genre": genre.value})
        print(response.json())
        self.assertIsNotNone(response)

    def test_router_find_all(self):
        size = 2
        unique = False
        genre = GenreEnum.male
        response = client.get("/persons", params={"size": size, "unique": unique, "genre": genre.value})
        print(response.json())
        self.assertEqual(len(response.json()), size)


if __name__ == '__main__':
    unittest.main()
