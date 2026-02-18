class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles

    def describe_car(self):
        print(f"{self.year} {self.brand} {self.model} with {self.mileage} miles.")

my_car = Car("Toyota", "Corolla", 2015)
print("Description of my car:")
my_car.describe_car()

print("\nDriving my car for 100 miles...")
my_car.drive(100)

print("\nDescribe my car after driving:")
my_car.describe_car()