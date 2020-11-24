from entity import Entity


class Company(Entity):
    def __init(self, businessName, company_address, company_Id):
        super().__init__(company_address, company_Id)
        self.businessName = businessName