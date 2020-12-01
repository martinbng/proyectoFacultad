from datetime import datetime, date, time, timedelta
import calendar
from entity import Entity


class Check:
    tags = ('Caducado','Extraviado','Robado')
    expires = 15

    def __init__(self, signature, memo , ammount, accountNumber, drawer, extension, tag = ''):
        self.tag = tag
        self.drawer = drawer            
        self.extension = extension         
        self.signature = signature
        self.memo = memo
        self.ammount = ammount
        self.accountNumber = accountNumber
        self.initialDate = datetime.now() #Toma la hora actual de la pc
        

    def __str__(self):
        return 'Librador: ' + str(self.drawer) + ' Destinatario: ' + str(self.extension) + \
        ' Firma: ' + self.signature + ' Motivo: ' + self.memo + ' Cantidad: ' + \
         str(self.ammount) + ' Numero de cuenta: ' + self.accountNumber
    

    def computes(self, finalDate):
        dif = finalDate - self.initialDate

        if dif.days >= 15:
            print(f'El cheque ha vencido con [{dif.days}] días')
            self.tag = self.tags[0]
        elif dif.days < 15:
            print(f'El cheque aún no ha vencido le faltan [{dif.days}] días para caducar')
