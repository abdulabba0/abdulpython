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
       
#     # car_name = "Tesla"
#     # car_model = "Model S"
#     # car_year = 2021
#     def turnLeft(self):
#         print(f"Car is turning left {self.car_dob}")
#     def turnRight(self):
#         print("Car is turning right")
#     def moveForward(self):
#         print("Car is moving forward")
#     def reverse(self):
#         print("Car is reversing")
# # Create an object of the Car class
# car1 = Car(2011, "Camry", "Toyota")

# print(car1.turnLeft())
# # print(car1.car_name)
# print(car1.car_model)
# print(car1.car_year)
# print(car1.turnLeft())
# print(car1.turnRight())
# print(car1.moveForward())
# print(car1.reverse())

class Laptop :
    def __init__(self, laptop_spec, laptop_type, laptop_year):
        print(f"My Laptop is {laptop_type} and {laptop_spec} from year {laptop_year}")
    def turnOn(self) :
        print("Laptop is turned on")
    def shutDown(self):
        print("Laptop is shut down")

Laptop = Laptop("12gen", "Gaming", 2024)
print(Laptop.turnOn())