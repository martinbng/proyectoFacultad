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


p1 = Person('Martin', 'Borges', 'Av. de las americas 123', '01')
p2 = Person('Juan','Rodriguez','Av. Andresito 109','02')

ch1 = Check('Mi firma', 'Envio de dinero para navidad',1200,'1234','24/11/20',p1, p2)
ch2 = Check('Mi firma', 'Envio de dinero para compras', 50000,'1234','24/11/20', p1, p2)
ch3 = Check('Mi firma','Envio de dinero para comprar un celular', 45000,'1234','24/11/20', p1, p2)

c1 = Account(usr1)
c1.checkRegister(ch1)
c1.checkRegister(ch2)
c1.checkRegister(ch3)

c2 = Account(usr2)


admin.accountRegister(c1)
admin.accountRegister(c2)


print(str(admin))