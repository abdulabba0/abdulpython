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

"Single inheritance"
class Vehicle:
    def __init__(self, name, type) :     
        self.name = name
        self.type = type
    def information(self):
        return f"This is a {self.type} named {self.name}"
    def quality(self):
        return f"{self.type} name {self.name}"
vehicle = Vehicle("Tesla", "Car")

print(vehicle.information())

class Car(Vehicle) :
    def __init__(self, car_year, car_model, car_name, name, type):
        super().__init__(name, type)
        self.car_name = car_name
        self.car_year = car_year
        self.car_model = car_model

    def Details(self):
        pass

    def turnLeft(self):
        print(f"{self.car_name} is turning left")
    def turnRight(self):
        print("Car is turning right")
    def moveForward(self):
        print("Car is moving forward")
    def reverse(self):
        print("Car is reversing")
# Create an object of the Car class
car = Car("Toyota", 2021, "Toyota", "Toyota", "car")
print(car.quality())

"Multi-Level Inheritance"
class Engine(Car):
    def __init__(self, engine_type, car_year, car_model, car_name, name, type):
        super().__init__(car_year, car_model, car_name, name, type)
        self.engine_type = engine_type

    def engine_details(self):
        return f"{self.engine_type} engine in a {self.car_year} {self.car_model} {self.car_name}, a {self.type} named {self.name}"

engine = Engine("V6", 2021, "Camry", "Toyota", "Toyota", "Car")
print(engine.engine_details())


"Multiple inheritance"
# class Parent1 :
#     def __init__(self, parent1Age, parent1name, parent1Hobby) :
#         self.parent1Age = parent1Age
#         self.parent1name = parent1name
#         self.parent1Hobby = parent1Hobby

#     def parentHobby(self):
#         return f"{self.parent1name} hobby is Reading {self.parent1Hobby}"
    
# class Parent2 :
#     def __init__(self, parent2Age, parent2name, parent2Hobby) :
#         self.parent2Age = parent2Age
#         self.parent2name = parent2name
#         self.parent2Hobby = parent2Hobby

#     def parent2hobby(self):
#         return f"{self.parent2name} hobby is {self.parent2Hobby}"
    
# class Child(Parent1, Parent2) :
#     def __init__(self, parent1Age, parent1name, parent1Hobby, parent2Age, parent2name, parent2Hobby):
#         Parent1.__init__(self, parent1Age, parent1name, parent1Hobby)
#         Parent2.__init__(self, parent2Age, parent2name, parent2Hobby)

# child = Child(88, "Frank", "Reading", 102, "Mary", "Cooking")

# print(child.parentHobby())
# print(child.parent2hobby())


# print(car1.turnLeft())
# print(car1.car_name)
# print(car1.car_model)
# print(car1.car_year)
# print(car1.turnLeft())
# print(car1.turnRight())
# print(car1.moveForward())
# print(car1.reverse())

# class Laptop :
    # laptop_spec = "Intel Core i5"
    # laptop_name = "Dell"
    # laptop_year = 2021
    # def __init__(self, laptop_spec, laptop_name, laptop_year):
    #     self.laptop_spec = laptop_spec
    #     self.laptop_name = laptop_name
    #     self.laptop_year = laptop_year
    
    # def specs(self) :
    #     print(f"{self.laptop_spec} has meant the requirements")
    # def name(self):
    #     print(f"{self.laptop_name} is shut down")
    # def year(self):
    #     print(f"Laptop is a {self.laptop_year}")

# Laptop1 = Laptop("i5", "HP", 2021)
# Laptop2 = Laptop("i7", "dell", 2024)

# print(Laptop1.laptop_year)
# print(Laptop1.laptop_name)
# print(Laptop1.laptop_spec)
# Laptop1.specs()
# Laptop1.name()
# Laptop1.year()

# print("-------------------------------------------------")
# Laptop2.laptop_name = "HP"
# Laptop2.laptop_spec = "14th Edition"
# Laptop2.laptop_year = 2023
# print(Laptop2.laptop_year)
# print(Laptop2.laptop_name)
# print(Laptop2.laptop_spec)
# Laptop2.specs()
# Laptop2.name()
# Laptop2.year()

