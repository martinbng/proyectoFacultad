from datetime import datetime, date, time, timedelta
import calendar
from entity import Entity


class Check:
    tags = ('Caducado','Extraviado','Robado')
    def __init__(self, signature, memo , ammount, accountNumber, drawer, extension):
        self.tags = None
        self.drawer = drawer            
        self.extension = extension         
        self.signature = signature
        self.memo = memo
        self.ammount = ammount
        self.accountNumber = accountNumber
        hoy = datetime.now() #Toma la hora actual de la pc
        self.finalDate = hoy + timedelta(days = 15)


    def __str__(self):
        return 'Librador: ' + str(self.drawer) + ' Destinatario: ' + str(self.extension) + \
        ' Firma: ' + self.signature + ' Motivo: ' + self.memo + ' Cantidad: ' + \
         str(self.ammount) + ' Numero de cuenta: ' + self.accountNumber
    

    def computes(self, finalDate):
        pcTime = datetime.now()


        if pcTime < finalDate:
            print('Quedan ' + finalDate - pcTime + ' dias antes que el cheque caduque')
        elif pcTime > finalDate:
            print('El cheque ha caducado con ' + finalDate.days() - pcTime.days() + ' dias de diferencia')
            self.tag = tags[0]
        elif pcTime == finalDate:
            print('El cheque caduda hoy')
            self.tag = tags[0]



