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
    def GlobalMovement(self):
        accumulate = 0

        for i in range(len(self.accounts)):
            for j in range(len(self.accounts[i].checks)):
                accumulate += self.accounts[i].checks[j].ammount

        return f'La cantidad total de dinero enviado en el sistema es de [${accumulate}]'


    def MainIssuers():
        pass

    
    def TotalIssuers(self):
        cont = 0
        for i in range(len(self.accounts)):
            cont += 1
        
        return f'Cantidad total de usuarios/ cuentas en el sistema [{cont}]'



    def GlobalChecks(self):
        cont = 0
        
        for i in range(len(self.accounts)):
            for j in range(len(self.accounts[i].checks)):
                cont += 1
        
        return f'Cantidad total de cheques en el sistema [{cont}]'


    def GlobalDrawerType():
        pass


    def GlobalGraph():
        pass