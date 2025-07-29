from faker import Faker
from faker.exceptions import UniquenessException

from src.repository.address_repository import find_one

fake = Faker('es_ES')


def find_all(count: int):
    result = []
    try:
        for i in range(count):
            number = i + 1
            item = find_one(fake, str(number))
            result.append(item)
    except UniquenessException:
        print("Error al obtener valores unicos, resetenado los valores únicos.")
        fake.unique.clear()
    return result
