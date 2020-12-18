from datetime import datetime, date, time, timedelta
import calendar
from entity import Entity
import hashlib 


class Check:
    tags = ('Caducado','Extraviado','Robado')
    expires = 15
    idCheck = 0
    def __init__(self, memo , ammount, drawer, extension,accountId = 0, signature = None):
        Check.idCheck += 1
        self.id = Check.idCheck
        self.accountId = accountId
        self.tag = ''
        self.drawer = drawer            
        self.extension = extension         
        self.signature = signature
        self.memo = memo
        self.ammount = ammount
        self.initialDate = datetime.now() #Toma la hora actual de la pc
        

    def __str__(self):
        return 'Librador: ' + str(self.drawer) + ' Destinatario: ' + str(self.extension) + \
        ' Firma: ' + self.signature + ' Motivo: ' + self.memo + ' Cantidad: ' + \
         str(self.ammount) + ' Numero de cheque: ' + str(self.id) + ' Numero de cuenta: c' +\
         str(self.accountId) + ' Fecha: ' + str(self.initialDate)
    
    
    #Toma el ID de la cuenta asociada al cheque
    def defineID(self,ID):
        self.accountId = ID

    #calcula si cheque vencio 
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

    #funcion que toma el nombre del usuario asociado a la cuenta y crea un hash con ella 
    def createSignature(self, signature):
        firma = str(self.drawer)
        self.signature = hashlib.md5(firma.encode())
        self.signature = self.signature.hexdigest()#firma digital


    #Envia la cantidad de dinero para un cheque
    def GiveCheckAmmount(self):
        return self.ammount
        

