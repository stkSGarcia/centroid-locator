import logging
import os

from flask import Flask, request

from impl.config import CONFIG
from impl.locator import locator
from impl.parser import parse

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/parse", methods=["GET", "POST"])
def parse_dxf():
    file = request.files["file"]
    path = os.path.join(CONFIG["workspace"]["store"], file.filename)
    file.save(path)
    logger.info(f"File received: {file.filename}.")
    response = parse(path)
    return [e.get_json() for e in response]


@app.route("/locate", methods=["GET", "POST"])
def locate():
    file = request.files["file"]
    path = os.path.join(CONFIG["workspace"]["store"], file.filename)
    file.save(path)
    dist = int(request.form["dist"])
    min_radius = int(request.form["min_radius"])
    max_radius = int(request.form["max_radius"])
    response = locator(path, dist, min_radius, max_radius)  # 90, (30, 60)
    return response
