import logging
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from app.dao import user as user_dao

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


class User(BaseModel):
    username: str
    passwd: str


class LoginResponse(BaseModel):
    code: int
    data: Optional[dict] = None
    msg: Optional[str] = None


@router.post("/login")
async def login(user: User) -> LoginResponse:
    code, name = user_dao.login(user.username, user.passwd)
    if code == 1:
        return LoginResponse(code=0, data={"username": user.username, "name": name})
    elif code == 0:
        return LoginResponse(code=0, msg="密码错误！")
    else:
        return LoginResponse(code=0, msg="当前用户不存在！")
