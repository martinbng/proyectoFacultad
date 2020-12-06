from entity import Entity


class Person(Entity):
    def __init__(self, name, surname, person_address):
        super().__init__(person_address)
        self.name = name

    
    def __str__(self):
        return self.name 