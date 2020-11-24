from entity import Entity


class Check:
    def __init__(self, signature, memo, ammount, accountNumber, date, finalDate):
        self.drawer = []               
        self.extension = []         
        self.signature = signature
        self.memo = None
        self.ammount = ammount
        self.accountNumber = accountNumber
        self.date = date
        self.finalDate = None


    #Agrega un librador a la lista
    def registerDrawer(self, librador):
        if isinstance(librador, Entity):
            self.drawer.append(librador)


    def registerExtension(self, recibidor):
        if isinstance(recibidor, Entity):
            self.extension.append(recibidor)


    def computes():
        pass