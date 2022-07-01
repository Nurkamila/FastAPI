from typing import Optional
import ormar
from sqlalchemy import PrimaryKeyConstraint
from db import MainMeta
from typing import Optional, Union, Dict
from user.models import User


class Follower(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    user: Optional[Union[User, Dict]] = ormar.ForeignKey(User, related_name="user")
    subscriber: Optional[Union[User, Dict]] = ormar.ForeignKey(User, related_name="subscriber")