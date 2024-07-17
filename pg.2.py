class Car:
    def __init__(self,make,fuel,milage):
        self.make=make
        self.fuel=fuel
        self.milage=milage
    def display(self):
        print(self.make)
        print(self.fuel)
        print(self.milage)

    def update(self,make,fuel,milage):
        self.make=make
        self.fuel=fuel
        self.milage=milage
c1=Car("hyundai","diesel",19)
c1.display()
c1.update("tata","petrol",10)
c1.display()
print()
make=input("enter make:")
fuel=input("enter fuel:")
milage=input("enter milage:")
c2=Car(make,fuel,milage)
print()
c2.display()
        
