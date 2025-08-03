import unittest

from src.exceptions.base_generic_exception import FakerUniqueValuesException
from src.mapper.person_mapper import map_person_male, map_person_female, map_person_male_unique, map_person_female_unique

class MyTestCase(unittest.TestCase):
    def test_map_person_male(self):
        result = map_person_male()
        print(result)
        self.assertIsNotNone(result)
    def test_map_person_female(self):
        result = map_person_female()
        print(result)
        self.assertIsNotNone(result)
    def test_map_person_male_unique(self):
        result = []
        size = 10
        for i in range(size):
            item = map_person_male_unique()
            result.append(item)

        self.assertEqual(len(result), size)
    def test_map_person_male_unique_error(self):
        result = []
        size = 500
        try:
            for i in range(size):
                item = map_person_male_unique()
                result.append(item)
        except FakerUniqueValuesException:
            print(f"Unexpected error was in test")
        self.assertNotEqual(len(result), size)
    def test_map_person_female_unique(self):
        result = []
        size = 10
        for i in range(size):
            item = map_person_female_unique()
            result.append(item)

        self.assertEqual(len(result), size)
    def test_map_person_female_unique_error(self):
        result = []
        size = 500
        try:
            for i in range(size):
                item = map_person_female_unique()
                result.append(item)
        except FakerUniqueValuesException:
            print(f"Unexpected error was in test")
        self.assertNotEqual(len(result), size)

if __name__ == '__main__':
    unittest.main()