import unittest

from src.mapper.address_mapper import map_address


class MyTestCase(unittest.TestCase):
    def test_map_address(self):
        result = map_address()
        print(result)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
