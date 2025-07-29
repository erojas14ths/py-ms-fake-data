from pydantic import BaseModel

class Person(BaseModel):
    id: str
    number: str
    first_name: str
    last_name: str
    email: str
    job: str
    phone_number: str