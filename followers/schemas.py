import uuid
from typing import List
from pydantic import BaseModel
from user.schemas import User


class FollowerCreate(BaseModel):
    user: str


class FollowerList(FollowerCreate):
    user: User
    subscriber: User

