# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:12:15 2019

@author: Yusef Quinlan
"""
#Create the 'vehicles' class, and make a setter method to set all attributes and
# a custom getter method to get all attributes.
class vehicles:
    def __init__(self,make,mpg):
        self.make = make
        self.mpg = mpg
        
    def set_all(self,make,mpg):
        self.make = make
        self.mpg = mpg
    def get_all(self):
        a = str(self.make)
        b = str(self.mpg)
        print("the make is:  " + a + "\n" + "the mpg is:  " + b + "\n")
 
#Test the class functions        
car1 = vehicles("Gord",900)
car1.get_all()
car1.set_all("Gord",23)
car1.get_all()
car1.set_all("Gird", 32)
car1.get_all()

#The cars class is created and it inherits all the functions and attributes of the 
# vehicles class, it also has a new function called 'printcars()'
class cars(vehicles):
    def printcars(self):
        print("This vehicle is a car, it has the following attributes and values: ")
        self.get_all()

#Testing of the inherited and none inherited functions of the 'cars' class
car2 = cars("Migmig",44)
car2.printcars()
car2.get_all()

#demonstrating that objects of the vehicles class cannot use the printcars() function 
# because it is not defined in the vehicles class.
# the Parent class 'vehicles' cannot inherit from the child class 'vehicles'
car1.printcars()

#creation of a new class called 'Trucks' that inherits its functions and attributes from the
# vehicles class, and also has its own function called 'printtrucks'
class Trucks(vehicles):
    def printtrucks(self):
        print("This vehicle is a truck, it has the following attributes and values: ")
        self.get_all()
        print("\n  THIS IS A TRUCK, MAKE SURE TO COMPLY WITH OUR COMPANY REGULATIONS ON TRUCKS!!!!")
 
#Testing the functions of the 'Trucks' class and also showing that objects of the 'Trucks' class
# cannot use the function printcars() as it has been defined in the 'cars' class and is not inherited
# by the 'Trucks' class.
Truck1 = Trucks("BigRig1.0", 15)
Truck1.printtrucks()
Truck1.get_all()
Truck1.printcars()
