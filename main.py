from account import Account
from user import User


class Main:
    def __init__(self):
       self.accounts = []
       "self.user = user"

    #Modulos para administrar el sistema

    #REGISTRA CUENTAS
    def accountRegister(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
 

    def __str__(self):
        c = ''
        for elements in range(len(self.accounts)):
            c += str(self.accounts[elements]) + '\n'

        return c

    
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