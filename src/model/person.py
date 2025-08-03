from pydantic import BaseModel

class Person(BaseModel):
    """Person model"""
    id: str
    first_name: str
    last_name: str
    name: str
    genre: str