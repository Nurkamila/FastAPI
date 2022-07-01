from fastapi import APIRouter
from user.api import on_after_register
from user.models import user_db
from user.auth import jwt_authentication, fastapi_users


user_router = APIRouter()


user_router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)

user_router.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)

user_router.include_router(
    fastapi_users.get_user_router(), prefix="/users", tags=["users"]
)