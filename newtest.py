from main import Main
from account import Account
from check import Check
from user import User
from person import Person


admin = Main()

usr1 = User('Martin12')
usr2 = User('Juan34')
usr3 = User('Lucas2')
usr4 = User('Pepito22')

c1 = Account(usr1)
c2 = Account(usr2)
c3 = Account(usr3)
c4 = Account(usr4)

admin.accountRegister(c1)
admin.accountRegister(c2)
admin.accountRegister(c3)
admin.accountRegister(c4)


p1 = Person('Martin','Borges','Av. de las americas')
p2 = Person('Pepe','Ramiresz','Av. Jose Ing')
p3 = Person('ELucas','Rodriguez','AV. andresito 129')
p4 = Person('Pepe','Sas','Misiones 120')


ch1 = Check('Para navidad',2000,p1,p2)
ch2 = Check('Para cumpleaños',3000,p1,p2)
ch3 = Check('Para FIESTA',3000,p3,p2)
ch4 = Check('Para cena',20000,p4,p3)


c1.checkRegister(ch1)
c1.checkRegister(ch2)

c2.checkRegister(ch3)
c2.checkRegister(ch4)

#Ver movimiento locales
print(c1.LocalMovement())

#ver movglobar
print(f'Mov global: {admin.GlobalMovement()}')
print(' ')
#Ver cantidad de cheuqes globales
print(f' La cantidad de chequess en el sistema es {admin.GlobalChecks()}')


#polimorfismo
"""
print(admin.GlobalOrLocalMovements('globral'))
print(admin.GlobalOrLocalMovements('local',us1.username))
print(admin.GlobalOrLocalMovements('ambos',usr2.username))
"""

#mostrando graficos
print(admin.GlobalGraph())