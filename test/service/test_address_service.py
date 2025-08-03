import unittest

from src.service.address_service import find_one, find_all


class MyTestCase(unittest.TestCase):
    def test_find_one(self):
        result = find_one()
        self.assertIsNotNone(result.id)

    def test_find_all(self):
        size = 10
        result = find_all(size)
        self.assertEqual(len(result), size)


if __name__ == '__main__':
    unittest.main()
