from main import Main
from account import Account
from user import User
from check import Check


#creando la administración
admin = Main()


#creando usuarios
c1 = Account()
c2 = Account()
c3 = Account()
c4 = Account()
c5 = Account()
c6 = Account()


#cheque
cheque = Check()


usr1 = User('Martin','1234contraseña')
usr2 = User('Junito','123juanito')
usr3 = User('Pepe12','contraseñaFacil')
usr4 = User('Carlo_Kpo','55kapo')
usr5 = User('Jose_ok','jose44')
usr6 = User('Lauta','contraseña')


#registrando usuarios
c1.userRegister(usr1)
c2.userRegister(usr2)
c3.userRegister(usr3)
c4.userRegister(usr4)
c5.userRegister(usr5)
c6.userRegister(usr6)



#registrando cuentas
admin.accountRegister(c1)
admin.accountRegister(c2)
admin.accountRegister(c3)
admin.accountRegister(c4)
admin.accountRegister(c5)
admin.accountRegister(c6)


print(str(admin.accounts))