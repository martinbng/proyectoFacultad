from entity import Entity


class Check:
    def __init__(self, signature, memo , ammount, accountNumber, date, drawer, extension):
        self.drawer = drawer            
        self.extension = extension         
        self.signature = signature
        self.memo = memo
        self.ammount = ammount
        self.accountNumber = accountNumber
        "self.date = date"
        "self.finalDate = finalDate"


    def __str__(self):
        return 'Librador: ' + str(self.drawer) + ' Destinatario: ' + str(self.extension) + \
        ' Firma: ' + self.signature + ' Motivo: ' + self.memo + ' Cantidad: ' + \
         str(self.ammount) + ' Numero de cuenta: ' + self.accountNumber
    

    def computes():
        pass