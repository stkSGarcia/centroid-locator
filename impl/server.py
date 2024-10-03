import logging
import os

from flask import Flask, request
from flask_cors import CORS

from impl.config import CONFIG
from impl.locator import locator
from impl.parser import parse
from impl.user import user

logger = logging.getLogger(__name__)
app = Flask(__name__)
CORS(app, resources=r"/*")
headers = {
    "Access-Control-Allow-Origin": "http://localhost:3000"
}

app.register_blueprint(user)


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


@app.route("/weldingInfo", methods=["GET"])
def welding_info():
    dictionary = [{"name": "电流", "data": "188"}, {"name": "电压", "data": "10.1"},
                  {"name": "焊接速度", "data": "300"}, {"name": "焊接距离", "data": "11.6"}]
    response = dictionary
    return response


@app.route("/uploadCAD", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file.save(os.path.join("/Users/jocelyn/Downloads/cad_lib", file.filename))
    return file.filename
