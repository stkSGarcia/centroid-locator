import logging
from typing import Optional, Annotated

from fastapi import APIRouter, Form
from pydantic import BaseModel

from app.dao import user as user_dao

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


class LoginData(BaseModel):
    username: str
    password: str


class RegisterData(BaseModel):
    username: str
    name: str
    password: str


class UserResponse(BaseModel):
    code: int
    data: Optional[dict] = None
    msg: Optional[str] = None


@router.post("/login")
async def login(data: Annotated[LoginData, Form()]) -> UserResponse:
    code, name = user_dao.login(username=data.username, password=data.password)
    if code == 1:
        return UserResponse(code=0, data={"username": data.username, "name": name})
    elif code == 0:
        return UserResponse(code=0, msg="密码错误！")
    else:
        return UserResponse(code=0, msg="当前用户不存在！")


@router.post("/register")
async def register(data: Annotated[RegisterData, Form()]) -> UserResponse:
    is_successful = user_dao.register(
        username=data.username, name=data.name, password=data.password
    )
    return UserResponse(code=0) if is_successful else UserResponse(code=1)
