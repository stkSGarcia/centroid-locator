from impl import database

class UserDao:
    def login(self,username,passwd):
        result = database.queryone("select name,passwd from users where username={username} and is_delete=0".format(username=username))
        if result == None:
            return None
        name = result[0]
        cur_passwd = result[1]
        if passwd == cur_passwd:
            return name
        return "-1"
