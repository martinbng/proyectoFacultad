

class Entity:
    idEntity = 0
    def __init__(self, address):
        Entity.idEntity += 1
        self.addres = address
        self.id = Entity.idEntity