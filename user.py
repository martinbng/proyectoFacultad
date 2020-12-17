

class User:
    idUser = 0
    def __init__(self, username, accountId = 0):
        User.idUser += 1
        self.id = User.idUser
        self.accountId = accountId
        self.username = username


    def __str__(self):
        return str(self.username)


    #Toma el ID de la cuenta asociada al usuario, así user sabe que pertenece a una cuenta
    def defineID(self,ID):
        self.accountId = ID