from main import Main
from account import Account
from user import User
from check import Check
from person import Person
from company import Company


#creando la administración
admin = Main()


usr1 = User('Martin','123contraseña')
usr2 = User('Juan', 'contraseña')


c1 = Account(usr1)
c2 = Account(usr2)

admin.accountRegister(c1)
admin.accountRegister(c2)


print(str(admin))