from account import Account
from user import User
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


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


    def MainIssuers(self):
        mainUser = self.accounts[0].checks[0].ammount
        lessUser = self.accounts[0].checks[1].ammount
        
        answer = [0,0]
        for i in range(len(self.accounts)):
            for j in range(len(self.accounts[i].checks)):
                if self.accounts[i].checks[j].ammount > mainUser:
                    answer[0] = self.accounts[i].user
                    mainUser = self.accounts[i].checks[j].ammount
                
                if self.accounts[i].checks[j].ammount < lessUser:
                    answer[1] = self.accounts[i].user
                    lessUser = self.accounts[i].checks[j].ammount

        return f'El usuario que más ha emitido fue: {answer[0]} con [{mainUser}] y el que menos: {answer[1]} con [{lessUser}]'
    

    def TotalIssuers(self):
        cont = 0
        names = ''

        for i in range(len(self.accounts)):
            names += str(self.accounts[i].user) + ', ' 
            cont += 1
        
        return f'Cantidad total de usuarios/ cuentas en el sistema [{cont}] y los nombres son: \n {names}'


    def GlobalChecks(self):
        cont = 0
        
        for i in range(len(self.accounts)):
            for j in range(len(self.accounts[i].checks)):
                cont += 1
        
        return f'Cantidad total de cheques en el sistema [{cont}]'


    def GlobalDrawerType(self):
        pass


    def GlobalGraph(self):
        #movimientos en función de usuarios en el sitema
        movements = list()
        names = list()

        for i in range(len(self.accounts)):
            if i <= len(self.accounts):
                names.append(0)
                movements.append(0)

            for j in range(len(self.accounts[i].checks)):
                movements[i] += self.accounts[i].checks[j].ammount

            names[i] = self.accounts[i].user

        fig, ax = plt.subplot()
        #Etiqueta en el eje Y
        ax.set_ylabel('Cantidad ($)')
        #Etiqueta en el eje X
        ax.set_xlabel('Usuario')
        
        #creo grafica
        plt.bar(str(names), int(movements))

        plt.show()