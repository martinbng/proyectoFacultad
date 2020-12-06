from datetime import datetime, date, time, timedelta
import calendar
from entity import Entity


class Check:
    tags = ('Caducado','Extraviado','Robado')
    expires = 15
    idCheck = 0
    def __init__(self, signature, memo , ammount, drawer, extension):
        Check.idCheck += 1
        self.id = Check.idCheck
        self.tag = ''
        self.drawer = drawer            
        self.extension = extension         
        self.signature = signature
        self.memo = memo
        self.ammount = ammount
        #agregar numero de cheques para una cuenta
        self.initialDate = datetime.now() #Toma la hora actual de la pc
        

    def __str__(self):
        return 'Librador: ' + str(self.drawer) + ' Destinatario: ' + str(self.extension) + \
        ' Firma: ' + self.signature + ' Motivo: ' + self.memo + ' Cantidad: ' + \
         str(self.ammount)
    

    def computes(self, finalDate):
        dif = finalDate - self.initialDate

        if dif.days >= 15:
            print(f'El cheque ha vencido con [{dif.days}] días')
            self.tag = self.tags[0]
        elif dif.days < 15:
            print(f'El cheque aún no ha vencido le faltan [{dif.days}] días para caducar')


    #Si cheque fue robado o extraviado
    def report(self, answer):
        answer = answer.lower()
        answer = answer.capitalize()
        if answer not in self.tags:
            raise ValueError('%s no es una respuesta valida' %answer)
        else:
            self.tag = answer


