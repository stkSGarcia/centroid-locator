from impl import database

class UserDao:
    def login(self):
        result = database.query("select * from users")
        print(result)
        return "123"