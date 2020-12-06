

class User:
    idUser = 0
    def __init__(self, username):
        User.idUser += 1
        self.id = User.idUser
        self.username = username


    def __str__(self):
        return str(self.username)