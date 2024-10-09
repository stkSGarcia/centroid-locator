import logging
from flask import Blueprint, request
from impl.dao.user import UserDao
from impl.json_response import JsonResponse

logger = logging.getLogger(__name__)

user = Blueprint('user',__name__)

@user.route('/user/login', methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username +" "+password)
    userDao = UserDao()
    name = userDao.login(username,password)
    if name == None:
        return JsonResponse.success(msg="当前用户不存在！").to_dict()
    if name == "-1":
        return JsonResponse.success(msg="密码错误！").to_dict()
    else:
        return JsonResponse.success(data={'username':username, 'name':name}).to_dict()

