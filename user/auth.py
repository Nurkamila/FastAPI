import uuid
from user.schemas import User, UserDB, UserCreate, UserUpdate
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from user.models import user_db  
import fastapi_users

SECRET = "83548e5a79eea2dcd4810435db02aa9dcc16f9c82b021bd6e9a309ea1602868c"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)

current_active_user = fastapi_users.current_user(active=True)


fastapi_users = FastAPIUsers[User, uuid.UUID](
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)


current_active_user = fastapi_users.current_user(active=True)