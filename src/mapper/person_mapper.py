from faker import Faker
from faker.exceptions import UniquenessException

from src.exceptions.base_generic_exception import FakerUniqueValuesException, BaseGenericException
from src.model.person import Person

fake = Faker('es_ES')


def map_person():
    """Map person model"""
    id = fake.uuid4()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    job = fake.job()
    phone_number = fake.phone_number()
    return Person(id=id,
                  first_name=first_name,
                  last_name=last_name,
                  email=email,
                  job=job,
                  phone_number=phone_number)


def map_person_unique():
    """Map person model with unique data"""
    try:
        id = fake.unique.uuid4()
        first_name = fake.unique.first_name()
        last_name = fake.unique.last_name()
        email = fake.unique.email()
        job = fake.unique.job()
        phone_number = fake.unique.phone_number()
        return Person(id=id,
                      first_name=first_name,
                      last_name=last_name,
                      email=email,
                      job=job,
                      phone_number=phone_number)
    except UniquenessException as ex:
        print(f"Unexpected error was: {ex}")
        print("Error getting unique values, resetting unique values.")
        fake.unique.clear()
        raise FakerUniqueValuesException
