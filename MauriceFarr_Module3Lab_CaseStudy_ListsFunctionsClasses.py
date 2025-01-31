#header information
"""
author: Maurice Farr
date: 1/30/2025
assignment: Module 3 Lab - Case Study: Lists, Functions, and Classes
purpose: We need to create a Python application that includes a main class called Vehicle, which has an attribute for the type of vehicle, like car, truck, plane, boat, or broomstick. 
There will be a subclass named Automobile that inherits from Vehicle and adds attributes for year, make, model, number of doors (either 2 or 4), and roof type (solid or sunroof). 
The application should take user input for a car, storing "car" in the Vehicle superclass's vehicle type. 
It will then prompt the user for the year, make, model, number of doors, and roof type, saving this information in the respective attributes. 
Finally, the app will display the information in a clear format, such as: Vehicle type: car, Year: 2022, Make: Toyota, Model: Corolla, Number of doors: 4, Type of roof: sunroof.
"""
#MauriceFarr_Module3Lab_CaseStudy_ListsFunctionsClasses.py

#Source Code of All Files:
import random

#Define the super class called Vehicle
class Vehicle:
    #Initialize the "Vehicle" object which includes an attribute for vehicle type (such as car, truck, plane, boat, or a broomstick)
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    #Display the information of the Vehicle
    def display_info(self):
        print("Vehicle Type: " + self.vehicle_type)  #Print the Vehicle type

#Define the Automobile class that inherits from the Vehicle class
class Automobile(Vehicle):
    #Initialize the Automobile object with the inherited attributes and additional attributes, including the year, make, model, doors (2 or 4), and roof (solid or sun roof)
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        #Call the constructor of the Vehicle to initialize inherited attributes
        super().__init__(vehicle_type)
        self.year = year  #Initialize the attribute for the year of the vehicle
        self.make = make  #Initialize the attribute for the make of the vehicle
        self.model = model #Initialize the attribute for the model of the vehicle
        self.doors = doors #Initialize the attribute for how many doors are on the vehicle
        self.roof = roof  #Initialize the attribute for the type of roof on the vehicle

    #Display the information of the Automobile
    def display_info(self):
        #Call the display_info method from the Vehicle class
        super().display_info()
        print("Year: " + str(self.year)) #Print the year of the vehicle
        print("Make: " + str(self.make)) #Print the make of the vehicle
        print("Model: " + str(self.model)) #Print the model of the vehicle
        print("Doors: " + str(self.doors)) #Print how many doors are on the vehicle
        print("Roof: " + str(self.roof)) #Print the type of roof on the vehicle

#Define the function of the vehicle app
def vehicle_app():
    #Ask the user to input the type of vehicle, in this case we will input "car"
    vehicle_type = input("Please enter the vehicle type: ")

    #Ask the user to input the Automobile attributes
    year = input("Please enter the year of the vehicle: ")
    make = input("Please enter the make of the vehicle: ")
    model = input("Please enter the model of the vehicle: ")
    doors = input("Please enter the total amount of doors on the vehicle (2 or 4): ")
    roof = input("Please enter the type of roof on the vehicle (solid or sun roof): ")

    #Create an instance of the Automobile
    user_automobile = Automobile(vehicle_type, year, make, model, doors, roof)

    #Display the information of the car
    user_automobile.display_info()

#Call the function to run the application
vehicle_app()
