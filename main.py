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
    
    #muestra movimientos globales
    def GlobalMovement(self):
        accumulate = 0

        for i in range(len(self.accounts)):
            accumulate += self.accounts[i].GiveAccountAmmount()

        return accumulate

    #muestra quienes fueron los que menos y más libraron cheques en el sistema
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
        return f'Cantidad total de usuarios/ cuentas en el sistema [{len(self.accounts)}] y los nombres son: \n {self.UsersNames()}'

    #cuenta la cantidad de cheques en el sistema
    def GlobalChecks(self):
        cont = 0
        
        for i in range(len(self.accounts)):
            cont += self.accounts[i].GiveQuantityOfChecks()
        
        return cont

    #muestra los tipos de libradores que hay en el sistema
    def GlobalDrawerType(self):
        cont = [0,0]
        for i in range(len(self.accounts)):
            for j in range(len(self.accounts[i].checks)):
                if isinstance(self.accounts[i].checks[j].drawer, Person):
                    cont[0] +=1
                elif isinstance(self.accounts[i].checks[j].drawer, Company):
                    cont[1] +=1
        
        return f'Hay [{cont[0]}] de libradores del tipo Persona y [{cont[1]}] del tipo Compañia'
        

    #muestra un grafico de los cheques por personas en el sistema
    def GlobalGraph(self):
        name = []
        performance = []
        for i in range(len(self.accounts)):
            name.append(self.accounts[i].user) 

        y_pos = np.arange(len(name))
        for i in range(len(self.accounts)):
            #performance.append(len(self.accounts[i].checks))
            performance.append(self.accounts[i].GiveQuantityOfChecks())

        plt.bar(y_pos, performance, align = 'center', alpha = 0.5, color = 'red')
        plt.xticks(y_pos, name)
        plt.ylabel('Cheques')
        plt.title('Cantidad de cheques por usuarios')

        return plt.show()


    #devuelve una lista con los nombres de los usuarios en el sistema
    def UsersNames(self):
        names = []
        for i in range(len(self.accounts)):
            names.append(str(self.accounts[i].user))
        
        return names
    

    #Funcion para tomar el index del nombre de un usuario así luego mostrar sus movimientos
    def TakeIndex(self,user):
        index = False
        
        if str(user) in self.UsersNames():
            index = self.UsersNames().index(user)
        
        return index
     

    #polimorfismo
    def GlobalOrLocalMovements(self, opc, user = None):
        opciones = ('global','local','ambos')
        opc = opc.lower()
        movmment = []

        if opc in opciones:
            if opc == opciones[0]:
                print('Movimientos globales: ')
                movmment.append(self.GlobalMovement())
            elif opc == opciones[1]:
                movmment.append( self.accounts[self.TakeIndex(user)].LocalMovement())
            elif opc == opciones[2]:
                movmment.append(self.GlobalMovement())
                movmment.append(self.accounts[self.TakeIndex(user)].LocalMovement())
                return f'El dinero total del sistema es: {movmment[0]} \n {movmment[1]}'

        return movmment

        