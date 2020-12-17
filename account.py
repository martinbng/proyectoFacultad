from check import Check
from user import User


class Account:
    idAccount = 0
    def __init__(self, user):
        Account.idAccount += 1
        self.id = Account.idAccount
        self.checks = []
        self.user = user
        self.user.defineID(self.GiveID())


    def checkRegister(self, check):
        if isinstance(check, Check):
             self.checks.append(check)
             for i in range(len(self.checks)):
                 self.checks[i].defineID(self.GiveID())#Envio el ID para esta cuenta a sus multiples cheques asociados
                 self.checks[i].createSignature(self.GiveSignature())


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


    def LocalChecks(self):
        return f'Cantidad de cheques en la cuenta de [{self.user}] son: [{len(self.checks)}]'


    #Envia el ID de una cuenta
    def GiveID(self):
        return self.id


    #Envia el nombre de la cuenta al cheque, así se crea una firma hash en cheque
    def GiveSignature(self):
        return self.user.username

    
    #Returna la cantidad de cheques que hay en una cuenta
    def GiveQuantityOfChecks(self):
        return len(self.checks)

    
    #Envia la cantidad de dinero emitido en una cuenta
    def GiveAccountAmmount(self):
        acm = 0
        for i in range(len(self.checks)):
            acm += int(self.checks[i].GiveCheckAmmount())
        
        return acm