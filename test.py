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


#SECCION DE CHEQUES
p1 = Person('Av. de las Americas 45','01')
p1.name = 'Martin'
p1.surname = 'Borges'

p2 = Person('Av. Andresito 23','02')
p2.name = 'Juan'
p2.surname = 'Rodriguez'

em1 = Company('Av. Misiones 365', '03')
em2 = Company('Av. Jose Ingenieros 23','04')

#creando parametros para cheque
ch1 = Check('MiFirma','Para navidad','1200$','1234','24/11/20')
ch1.registerDrawer(p1)
ch1.registerExtension(p2)

ch2 = Check('MiFirma','Para comprar televisor','50000$','1234','24/11/20')


c1 = Account(usr1)
c1.checkRegister(ch1)
c1.checkRegister(ch2)

c2 = Account(usr2)


admin.accountRegister(c1)
admin.accountRegister(c2)


print(str(admin))