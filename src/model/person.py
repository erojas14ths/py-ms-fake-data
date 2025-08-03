from pydantic import BaseModel

class Person(BaseModel):
    """Person model"""
    id: str
    first_name: str
    last_name: str
    email: str
    job: str
    phone_number: str