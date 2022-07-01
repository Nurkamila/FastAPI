import uuid
from fastapi_users import schemas
from typing import Optional

from pydantic import EmailStr


class User(schemas.BaseUser[uuid.UUID]):
    username: str


class UserCreate(schemas.CreateUpdateDictModel):
    username: str
    email: EmailStr
    password: str


class UserUpdate(User, schemas.BaseUserUpdate):
    pass


class UserDB(User, schemas.BaseUserDB):
    pass