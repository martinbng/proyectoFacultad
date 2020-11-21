from entity import Entity


class Check:
    def __init(self, signature, memo, ammount, accountNumber, date, finalDate):
        self.drawer = []               
        self.extensions = []         
        self.signature = signature
        self.memo = memo
        self.ammount = ammount
        self.accountNumber = accountNumber
        self.date = date
        self.finalDate = None
    
    
    #mostrando el cheque
    def __str__(self):
        if self.drawer != None:
            return self.drawer.name + 'Apellido: ' + self.drawer.surname


    def computes():
        pass