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

ch1 = Check('Para navidad',2000,p1,p2)
ch2 = Check('Para cumpleaños',3000,p1,p2)

c1.checkRegister(ch1)
c1.checkRegister(ch2)


print(f'la cantidad de cheques en el sistema es de [{admin.GlobalChecks()}]')
#print(admin.GlobalGraph())

#ver la firma
print(f'La firma para este cheque es: {ch1.signature}')
print(admin.GlobalGraph())

print(f'La cuenta ha emitido un total de {c1.GiveAccountAmmount()}$')
print(f'La cantidad de dinero emitido en el sistema es de {admin.GlobalMovement()}$')

#si muestro un cheque
print(ch1)

#si muestro un usuario
print(usr1)