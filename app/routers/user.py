import logging

from fastapi import APIRouter
from pydantic import BaseModel

from app.dao.user import UserDao
from app.json_response import JsonResponse

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


class User(BaseModel):
    username: str
    passwd: str


@router.post("/login")
async def login(user: User):
    name = UserDao().login(user.username, user.passwd)
    if name is None:
        return JsonResponse.success(msg="当前用户不存在！").to_dict()
    if name == "-1":
        return JsonResponse.success(msg="密码错误！").to_dict()
    else:
        return JsonResponse.success(data={'username': user.username, 'name': name}).to_dict()
