from main import Main
from account import Account
from check import Check
from user import User
from person import Person


admin = Main()

usr1 = User('Martin12')
usr2 = User('Juan34')

c1 = Account(usr1)
c2 = Account(usr2)

admin.accountRegister(c1)
admin.accountRegister(c2)


p1 = Person('Martin','Borges','Av. de las americas')
p2 = Person('Pepe','Ramiresz','Av. Jose Ing')

ch1 = Check('Mi forma','Para navidad',2000,p1,p2)
ch2 = Check('Mi firma','Para cumpleaños',3000,p1,p2)

c1.checkRegister(ch1)
c1.checkRegister(ch2)

print(f'la cantidad de cheques en el sistema es de [{admin.GlobalChecks()}]')
print(admin.GlobalGraph())