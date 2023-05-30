class house():
    """класс следует принципу srp, он отвечает за общую концепцию дома и его постройке."""
    def __init__(self, number, street):
     self.number = number
     self.street = street
    def build (self):
        return("Дом на улице "+self.street+" под номером "+ self.number +" Построен.")

"""класс следует принципу srp, он отвечает за информацию о квртирном доме, 
    и о его постройке. также соответсвует принципу lsp, 
    дочерный класс не только выполняет поведение родительского класса, 
    но и дополняет свои функции."""
class apartment_house(house):
    
    def __init__(self, number, street, organization):
        super().__init__(number, street)
        self.organization = organization
    def print_info (self):
        return (self.organization,self.street,self.number)
    def build(self):
          return super().build()

    """класс следует принципу srp, он отвечает за информацию о квртирном доме, 
    и о его постройке. также соответсвует принципу lsp, 
    дочерный класс не только выполняет поведение родительского класса, 
    но и дополняет свои функции."""
class private_house(house):
    def __init__(self, number, street, owner):
        super().__init__(number,street)
        self.__owner = owner
    def print_info (self):
        return (self.__owner,self.street,self.number)
    def build(self):
        return super().build()
    
house = house("33","Ленина")
house1 = apartment_house("12","Рокоссовсокго",'ООО "Мишино"' )
house2 = private_house("23", "Победы","Иванов Иван Иванович")

print (house.build())
print (house1.build())
print (house2.build())
print (house1.print_info(), house2.print_info())