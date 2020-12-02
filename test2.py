from datetime import datetime, date, time, timedelta
import calendar


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

p3 = Person('Anestecio','Rodriguez','Jose ingenieros 90','03')
p4 = Person('Lautaro','Baez','Av. Guayaba 10','04')

ch1 = Check('Mi firma', 'Envio de dinero para navidad',1200,'1234',p1, p2)
ch2 = Check('Mi firma', 'Envio de dinero para compras', 50000,'1234', p1, p2)
ch3 = Check('Mi firma','Envio de dinero para comprar un celular', 45000,'1234', p1, p2)

ch4 = Check('Firmado','Envio de dinero para vacaciones',12000,'133',p3,p4)
ch5 = Check('Firmado','Envio de dinero para comprar auto',1200000,'133', p3, p4)

c1 = Account(usr1)
c1.checkRegister(ch1)
c1.checkRegister(ch2)
c1.checkRegister(ch3)

c2 = Account(usr2)
c2.checkRegister(ch4)
c2.checkRegister(ch5)


admin.accountRegister(c1)
admin.accountRegister(c2)

futuro = datetime.now() + timedelta(days=15)

print(ch1.computes(futuro))
print(ch1.tag)

ch1.report('extraviado')
print(ch1.tag)

#muestra total de cheques y usuarios en el sistema
print(admin.TotalIssuers())
print(admin.GlobalChecks())


#Muestra la cantidad de cheques para una cuenta en especifico
print(c1.LocalChecks())


#muestra movimientos del sistema
print(admin.GlobalMovement())


#muestra los movimientos para una cuenta
print(c1.LocalMovement())


#muestra usuarios principales
print(admin.MainIssuers())


grafico = admin.GlobalGraph()
