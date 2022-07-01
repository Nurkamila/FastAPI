from fastapi import APIRouter, Depends
from user.auth import current_active_user
from schemas import FollowerCreate, FollowerList
from followers.models import Follower
from user.models import User
from typing import List

follower_router = APIRouter(prefix='followers')


@follower_router.post('/', status_code=201)
async def add_follower(
    schema: FollowerCreate, user: User = Depends(current_active_user)
):
    host = await User.objects.get(id=schema.user)
    return await Follower.objects.create(subscriber=user.dict(), user=host)


@follower_router.get('/me', response_model=List[FollowerList])
async def my_list_follower(user: User = Depends(current_active_user)):
    return await Follower.objects.filter(user=user).all()


@follower_router.post('/me', response_model=List[FollowerList])
async def my_list_follower(user: User = Depends(current_active_user)):
    return await Follower.objects.filter(user=user).all()