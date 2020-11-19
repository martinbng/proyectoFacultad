from account import Account
from user import User


class Main:
    def __init__(self):
       self.accounts = []
       self.users = []


    #Modulos para administrar el sistema

        #REGISTRA USUARIOS
    def userRegister(self, user):
        if isinstance(user, User):
            self.users.append(user)


    #Modulos de los requerimientos


    def GlobalMovement():
        pass


    def MainIssuers():
        pass

    
    def TotalIssuers():
        pass


    def GlobalChecks():
        pass


    def GlobalDrawerType():
        pass


    def GlobalGraph():
        pass