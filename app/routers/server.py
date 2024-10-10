import logging
import os
from typing import Annotated

from fastapi import APIRouter, File, UploadFile, Form

from app.config import CONFIG
from app.locator import locator
from app.parser import parse

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/server",
    tags=["server"],
)


@router.post("/parse")
async def parse_dxf(file: UploadFile):
    logger.info(f"File received: {file.filename}.")
    path = os.path.join(CONFIG["workspace"]["store"], file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())
    response = parse(path)
    return [e.get_json() for e in response]


@router.post("/locate")
async def locate(file: Annotated[UploadFile, File()],
                 dist: Annotated[int, Form()],
                 min_radius: Annotated[int, Form()],
                 max_radius: Annotated[int, Form()]):
    logger.info(f"File received: {file.filename}.")
    path = os.path.join(CONFIG["workspace"]["store"], file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())
    response = locator(path, dist, min_radius, max_radius)  # 90, (30, 60)
    return response


@router.get("/weldingInfo")
async def welding_info():
    dictionary = [{"name": "电流", "data": "188"}, {"name": "电压", "data": "10.1"},
                  {"name": "焊接速度", "data": "300"}, {"name": "焊接距离", "data": "11.6"}]
    response = dictionary
    return response


@router.post("/uploadCAD")
async def upload_file(file: UploadFile):
    with open(os.path.join("/Users/jocelyn/Downloads/cad_lib", file.filename), "wb") as f:
        f.write(file.file.read())
    return file.filename
