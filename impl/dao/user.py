from impl.database import Database

class UserDao:
    def login(self,username,passwd):
        with Database() as db:
            result = db.queryone(f"select name, passwd from users where username={username} and is_delete=0")
        if result is None:
            return None
        name = result[0]
        cur_passwd = result[1]
        if passwd == cur_passwd:
            return name
        return "-1"
