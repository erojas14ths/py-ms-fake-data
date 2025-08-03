from fastapi import APIRouter, Query

from src.constants.fake_constants import GENRE_MALE
from src.enums.genre_enum import GenreEnum
from src.model.person import Person
from src.service.person_service import find_one as find_one_service, find_all as find_all_service

router = APIRouter()


@router.get("/person")
def router_find_one(genre: GenreEnum = Query(default=GenreEnum.male)) -> Person:
    return find_one_service(genre)


@router.get("/persons")
def router_find_all(size: int = 0, unique: bool = False, genre: GenreEnum = Query(default=GenreEnum.male)) -> list[Person]:
    return find_all_service(size, unique, genre)
