from faker import Faker
from faker.exceptions import UniquenessException

from src.enums.genre_enum import GenreEnum
from src.exceptions.base_generic_exception import FakerUniqueValuesException
from src.model.person import Person

fake = Faker('es_ES')


def map_person_male():
    """Map person male model"""
    id = fake.uuid4()
    first_name = fake.first_name_male()
    last_name = fake.last_name_male()
    name = fake.name_male()
    genre = GenreEnum.male.value
    return Person(id=id,
                  first_name=first_name,
                  last_name=last_name,
                  name=name,
                  genre=genre)


def map_person_female():
    """Map person female model"""
    id = fake.uuid4()
    first_name = fake.first_name_female()
    last_name = fake.last_name_female()
    name = fake.name_female()
    genre = GenreEnum.female.value
    return Person(id=id,
                  first_name=first_name,
                  last_name=last_name,
                  name=name,
                  genre=genre)


def map_person_male_unique():
    """Map person male model with unique data"""
    try:
        id = fake.unique.uuid4()
        first_name = fake.unique.first_name_male()
        last_name = fake.unique.last_name_male()
        name = fake.unique.name_male()
        genre = GenreEnum.male.value
        return Person(id=id,
                      first_name=first_name,
                      last_name=last_name,
                      name=name,
                      genre=genre)
    except UniquenessException as ex:
        print(f"Unexpected error was: {ex}")
        print("Error getting unique values, resetting unique values.")
        fake.unique.clear()
        raise FakerUniqueValuesException


def map_person_female_unique():
    """Map person female model with unique data"""
    try:
        id = fake.unique.uuid4()
        first_name = fake.unique.first_name_female()
        last_name = fake.unique.last_name_female()
        name = fake.unique.name_female()
        genre = GenreEnum.female.value
        return Person(id=id,
                      first_name=first_name,
                      last_name=last_name,
                      name=name,
                      genre=genre)
    except UniquenessException as ex:
        print(f"Unexpected error was: {ex}")
        print("Error getting unique values, resetting unique values.")
        fake.unique.clear()
        raise FakerUniqueValuesException
