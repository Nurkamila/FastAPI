from typing import List
from urllib import response
from urllib.request import Request
from anyio import open_file
from user.auth import current_active_user
from fastapi import BackgroundTasks, Depends, UploadFile, File, APIRouter, Form
from starlette.responses import StreamingResponse
from video.services import save_video
from video.models import User, Video
from video.schemas import GetListVideo


video_router = APIRouter(tags=['video'])
 
@video_router.post('/video')
async def create_video(
    back_tasks: BackgroundTasks,
    title: str = Form(...), 
    description: str = Form(...),
    file: UploadFile = File(...),
    user: User = Depends(current_active_user)
):
    user = await User.objects.first()
    return await save_video(user, file, title, description, back_tasks)


# @video_router.get('/video/{video_pk}')
# async def get_video(video_pk: int):
#     file = await Video.objects.select_related('user').get(pk=video_pk)
#     file_like = open(file.file, mode="rb")
#     return StreamingResponse(file_like, media_type="video/mp4")


@video_router.get("/user/{user_pk}", response_model=List[GetListVideo])
async def get_list_video(user_pk: str):
    video_list = await Video.objects.filter(user=user_pk).all()
    return video_list


@video_router.get('/video/{video_pk}')
async def get_streaming_video(request: Request, video_pk: int):
    file, status_code, content_length, headers = await open_file(request, video_pk)
    response = StreamingResponse(
        file,
        media_type='video/mp4', 
        status_code=status_code,
    )

    response.headers.update({
        "Accept-Ranges": 'bytes',
        'Content-Length': str(content_length),
        **headers,
    })
    return response
