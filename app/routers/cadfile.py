import logging
import os
from typing import Optional, Annotated

from fastapi import APIRouter, Form, UploadFile
from pydantic import BaseModel

from app.dao import cadfile as cadfile_dao

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/cad",
    tags=["cad"],
)


# 用于支持模糊筛选
class ListData(BaseModel):
    name: str
    createuser: str


class AddCADData(BaseModel):
    name: str
    description: str
    username: str
    file: UploadFile


class CADResponse(BaseModel):
    code: int
    data: Optional[dict] = None
    msg: Optional[str] = None


@router.post("/list")
async def login(data: Annotated[ListData, Form()]) -> CADResponse:
    code, list = cadfile_dao.list(name=data.name, createuser=data.createuser)
    if code == 0:
        return CADResponse(code=0, data=list)
    else:
        return CADResponse(code=0, msg="当前无CAD文件！")


@router.post("/addcad")
async def register(data: Annotated[AddCADData, Form()]) -> CADResponse:
    location = "/Users/jocelyn/Downloads/cad_lib"
    with open(
        os.path.join(location, data.file.filename), "wb"
    ) as f:
        filedata = await data.file.read()
        f.write(filedata)

    is_successful = cadfile_dao.add(
        name=data.name, description=data.description, username=data.username,location=location+data.file.filename
    )

    return CADResponse(code=0) if is_successful else CADResponse(code=1)


# name: str
#     location: str
#     description: str
#     create_user_id: int
