from account import Account
from user import User


class Main:
    def __init__(self):
       self.accounts = []
       self.users = []


    #Modulos para administrar el sistema

    #REGISTRA CUENTAS
    def accountRegister(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
 

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