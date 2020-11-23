from main import Main
from account import Account
from user import User
from check import Check
from person import Person
from company import Company


#creando la administración
admin = Main()


#creando cuentas
c1 = Account()
c2 = Account()
c3 = Account()
c4 = Account()
c5 = Account()
c6 = Account()


#creando cheques
ch1 = Check()
ch2 = Check()
ch2 = Check()


    #Usuarios
usr1 = User('Martin','1234contraseña')
usr2 = User('Junito','123juanito')
usr3 = User('Pepe12','contraseñaFacil')
usr4 = User('Carlo_Kpo','55kapo')
usr5 = User('Jose_ok','jose44')
usr6 = User('Lauta','contraseña')


    #Personas
p1 = Person('Av. De las americas','1234')
p1.name = 'Martin'
p1.surname = 'Borges'

p2 = Person('Av. Andresito 123', '12345')
p2.name = 'Juanito'
p2.surname = 'Mendez'


    #Empresas
em1 = Company('Juan Manuel de Rosas 123', '12')
em1.businessName = 'Sport Gim'

em2 = Company('Av. Misiones 981','32')
em2.businessName = 'Bercomat'


    #Cheque
"p11 le envia dinero a p2"
ch1.registerDrawer(p1)
ch1.registerExtension(p2)


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


#registrando cheques dentro de una cuenta
c1.checkRegister(ch1)
c1.checkRegister(ch2)

"print(c1.checks)"
"print(str(admin.accounts))"