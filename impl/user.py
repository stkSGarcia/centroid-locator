import logging
from flask import Blueprint
from impl.dao.user import UserDao
logger = logging.getLogger(__name__)

user = Blueprint('user',__name__)

@user.route('/user/login', methods=["POST"])
def login():
    # dictionary = [{"name":"电流","data":"188"},{"name":"电压","data":"10.1"},{"name":"焊接速度","data":"300"},{"name":"焊接距离","data":"11.6"}]
    # response = dictionary
    userDao = UserDao()
    return userDao.login()
