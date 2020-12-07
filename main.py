from account import Account
from user import User
from person import Person
from company import Company

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


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
        names = ''
        for i in range(len(self.accounts)):
            names += str(self.accounts[i].user) + ', ' 

        return f'Cantidad total de usuarios/ cuentas en el sistema [{len(self.accounts)}] y los nombres son: \n {names}'


    def GlobalChecks(self):
        cont = 0
        
        for i in range(len(self.accounts)):
            cont += len(self.accounts[i].checks)
        
        return cont


    def GlobalDrawerType(self):
        cont = [0,0]
        for i in range(len(self.accounts)):
            for j in range(len(self.accounts[i].checks)):
                if isinstance(self.accounts[i].checks[j].drawer, Person):
                    cont[0] +=1
                elif isinstance(self.accounts[i].checks[j].drawer, Company):
                    cont[1] +=1
        
        return f'Hay [{cont[0]}] de libradores del tipo Persona y [{cont[1]}] del tipo Compañia'
        

    def GlobalGraph(self):
        name = [0,0]
        for i in range(len(self.accounts)):
            name[i] = self.accounts[i].user

        y_pos = np.arange(len(name))
        performance = [len(self.accounts[0].checks),len(self.accounts[1].checks)]

        plt.bar(y_pos, performance, align = 'center', alpha = 0.5)
        plt.xticks(y_pos, name)
        plt.ylabel('Cheques')
        plt.title('Cantidad de cheques por usuarios')

        return plt.show()