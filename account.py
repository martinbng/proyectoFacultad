from check import Check
from user import User


class Account:
   def __init__(self, user):
        self.checks = []
        self.user = user


   def checkRegister(self, check):
        if isinstance(check, Check):
             self.checks.append(check)


   def __str__(self):
        chain = ''

        for i in range(len(self.checks)):
             chain += str(self.checks[i]) + '\n'

        return chain


   def LocalMovement():
        pass


   def LocalChecks():
        pass


   def LocalGraph():
        pass