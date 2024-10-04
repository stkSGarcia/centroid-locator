import logging
import os

from fastapi import APIRouter

from app.config import CONFIG
from app.locator import locator
from app.parser import parse

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/server",
    tags=["server"],
)


@router.post("/parse")
async def parse_dxf():
    file = request.files["file"]
    path = os.path.join(CONFIG["workspace"]["store"], file.filename)
    file.save(path)
    logger.info(f"File received: {file.filename}.")
    response = parse(path)
    return [e.get_json() for e in response]


@router.post("/locate")
async def locate():
    file = request.files["file"]
    path = os.path.join(CONFIG["workspace"]["store"], file.filename)
    file.save(path)
    dist = int(request.form["dist"])
    min_radius = int(request.form["min_radius"])
    max_radius = int(request.form["max_radius"])
    response = locator(path, dist, min_radius, max_radius)  # 90, (30, 60)
    return response


@router.get("/weldingInfo")
async def welding_info():
    dictionary = [{"name": "电流", "data": "188"}, {"name": "电压", "data": "10.1"},
                  {"name": "焊接速度", "data": "300"}, {"name": "焊接距离", "data": "11.6"}]
    response = dictionary
    return response


@router.post("/uploadCAD")
async def upload_file():
    file = request.files["file"]
    file.save(os.path.join("/Users/jocelyn/Downloads/cad_lib", file.filename))
    return file.filename
