class Vehicles:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_make_model(self):
        print( f"I am driving {self.make} {self.model} ...")
    
    def move(self):
        print("I am moving ...")



my_car = Vehicles("Tesla", "Model 3")
print(my_car.make)
print(my_car.model)
my_car.move()
my_car.get_make_model()


my_car2 = Vehicles("Porche", "mustang")
print(my_car2.make)
print(my_car2.model)
my_car2.move()
my_car2.get_make_model()

# inheritance

class Airplane(Vehicles):
    def __init__(self,make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def move(self):
        print("I am flying ...")

class Truck(Vehicles):
    def move(self):
        print('Rumbles on ...')

class GolfCart(Vehicles):
    pass


my_truck = Truck("Ford", "F150")
my_truck.move()
my_truck.get_make_model()


my_golfcart = GolfCart("Volkswagen", "Golf")
my_golfcart.move()
my_golfcart.get_make_model()

my_airplane = Airplane("Boeing", 747, "N12345")
my_airplane.move()
my_airplane.get_make_model()



# polymorphism   same method name but different behavior


print('\n\n')

for v in (my_car, my_car2, my_airplane, my_truck, my_golfcart):
    v.get_make_model()
    v.move()