from check import Check
from user import User


class Account:
   def __init__(self):
        self.checks = []
        self.users = []

    
   def userRegister(self, user):#toma el parametro "user" de la instancia
        if isinstance(user, User):#Verifica que el parametro "user" sea instanciable en User
             self.users.append(user)#carga en la lista de usuarios al nuevo "user"


   def checkRegister(self, check):
        if isinstance(check, Check):
             self.checks.append(check)


   def LocalMovement():
        pass


   def LocalChecks():
        pass


   def LocalGraph():
        pass