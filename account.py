from check import Check
from user import User


class Account:
    idAccount = 0
    def __init__(self, user):
        Account.idAccount += 1
        self.id = Account.idAccount
        self.checks = []
        self.user = user


    def checkRegister(self, check):
        if isinstance(check, Check):
             self.checks.append(check)


    def __str__(self):
        chain = ''

        for i in range(len(self.checks)):
             chain += str(self.checks[i]) + '\n'

        return chain


    def LocalMovement(self):
        accumulate = 0

        for elements in range(len(self.checks)):
             accumulate += self.checks[elements].ammount

        return f'La cantidad de dinero que ha enviado [{self.user}] fue un total de: [${accumulate}]'


    def LocalChecks(self,):
        cont = 0

        for i in range(len(self.checks)):
             cont += 1
          
        return f'Cantidad de cheques en la cuenta de [{self.user}] son: [{cont}]'


    def LocalGraph():
        pass