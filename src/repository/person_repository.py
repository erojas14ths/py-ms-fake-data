from faker import Faker

from src.model.person import Person


def find_one(fake: Faker, number: str, unique: bool):
    if unique == True:

        id = fake.unique.uuid4()
        first_name = fake.unique.first_name()
        last_name = fake.unique.last_name()
        email = fake.unique.email()
        job = fake.unique.job()
        phone_number = fake.unique.phone_number()
        return Person(id=id,
                      number=number,
                      first_name=first_name,
                      last_name=last_name,
                      email=email,
                      job=job,
                      phone_number=phone_number)
    else:
        id = fake.uuid4()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        job = fake.job()
        phone_number = fake.phone_number()
        return Person(id=id,
                      number=number,
                      first_name=first_name,
                      last_name=last_name,
                      email=email,
                      job=job,
                      phone_number=phone_number)
