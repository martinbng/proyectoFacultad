from main import Main
from account import Account
from user import User

#creando la administración
admin = Main()


#creando usuarios
cuenta = Account()


Martin = User('Martin','1234contraseña')
Juan = User('Junito','123juanito')
Pepe = User('Pepe12','contraseñaFacil')
Carlo = User('Carlo_Kpo','55kapo')
Jose = User('Jose_ok','jose44')
Lautaro = User('Lauta','contraseña')


#registrando un usuario
admin.userRegister(Juan)
