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

