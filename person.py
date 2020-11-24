from entity import Entity


class Person(Entity):
    def __init__(self, name, surname, person_address, person_Id):
        super().__init__(person_address, person_Id)
        self.name = name
        self.surname = surname

    
    def __str__(self):
        return self.name + self.surname 