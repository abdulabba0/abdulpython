"""
A class is an object that represents

Object : Car
    car_name = "Tesla
    car_model = "Model S"
    car_year = 2021
    engine

    perform some actions
    move forward
    reverse
    turn left
    turn right
    play music

    __init__
"""

# class Car :
#     x = 5 # Feature of the object
#     def turnLeft(self):
#         print("Car is turning left")
# # Create an object of the Car class
# car1 = Car()

# print(car1.x)
# print(car1.turnLeft())

# class Car :
#     def __init__(self, car_year, car_model, car_name):
#         print(f"This is my car {car_year} and {car_model} and {car_name}")
#         self.car_dob = car_year
       
    # car_name = "Tesla"
    # car_model = "Model S"
    # car_year = 2021
    # def turnLeft(self):
    #     print(f"Car is turning left {self.car_dob}")
#     def turnRight(self):
#         print("Car is turning right")
#     def moveForward(self):
#         print("Car is moving forward")
#     def reverse(self):
#         print("Car is reversing")
# # Create an object of the Car class
# car1 = Car(2011, "Camry", "Toyota")

# print(car1.turnLeft())
# print(car1.car_name)
# print(car1.car_model)
# print(car1.car_year)
# print(car1.turnLeft())
# print(car1.turnRight())
# print(car1.moveForward())
# print(car1.reverse())

class Laptop :
    # laptop_spec = "Intel Core i5"
    # laptop_name = "Dell"
    # laptop_year = 2021
    def __init__(self, laptop_spec, laptop_name, laptop_year):
        self.laptop_spec = laptop_spec
        self.laptop_name = laptop_name
        self.laptop_year = laptop_year
    
    def specs(self) :
        print(f"{self.laptop_spec} has meant the requirements")
    def name(self):
        print(f"{self.laptop_name} is shut down")
    def year(self):
        print(f"Laptop is a {self.laptop_year}")

Laptop1 = Laptop("i5", "HP", 2021)
Laptop2 = Laptop("i7", "dell", 2024)

print(Laptop1.laptop_year)
print(Laptop1.laptop_name)
print(Laptop1.laptop_spec)
Laptop1.specs()
Laptop1.name()
Laptop1.year()

print("----------------------------------------------------------------")
# Laptop2.laptop_name = "HP"
# Laptop2.laptop_spec = "14th Edition"
# Laptop2.laptop_year = 2023
print(Laptop2.laptop_year)
print(Laptop2.laptop_name)
print(Laptop2.laptop_spec)
Laptop2.specs()
Laptop2.name()
Laptop2.year()