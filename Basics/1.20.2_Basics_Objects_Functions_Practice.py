# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:27:17 2019

@author: Yusef Quinlan
"""

#defining the bus class with setters and  getters for each attribute
class bus:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def get_name(self):
        return self.name
    def set_name(self, newName):
        self.name = newName
    def get_model(self):
        return self.model
    def set_model(self, newModel):
        self.model = newModel

#creating bus class objects        
bus1 = bus("A95","SomeModel")
bus2 = bus("A17", "Somemoodel")

#testing the setter and getter functions
bus1.get_name()
bus1.set_name("Jenny 77")
bus1.get_model()
bus1.set_model("SUPERBUS!")

bus1.get_name()
bus1.get_model()

bus2.get_name()
bus2.set_name("GG")
bus2.get_model()
bus2.set_model("Badbus :( ")

bus2.get_name()
bus2.get_model()

# re-defining the bus class but with a set_all and get_all function that can set all the attritubes
# to some specified argument value, and that can get all the attributes instead of having to get or set
# attributes individually.
class bus:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def get_name(self):
        return self.name
    def set_name(self, newName):
        self.name = newName
    def get_model(self):
        return self.model
    def set_model(self, newModel):
        self.model = newModel
    def get_all(self):
        d = str(self.name)
        e = str(self.model)
        f = d + " " + e
        return f
    def set_all(self, newName, newModel):
        self.name = newName
        self.model = newModel
#Object of type bus and testing of the new functions        
bus1 = bus("A95","SomeModel")


bus1.set_all("B66", "DEEZUL")
bus1.get_all()

# re-defined bus class with an altered getter method that more demonstrates more effectively what attributes
# are being returned and which piece of text relates to which bus attribute.

class bus:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def get_name(self):
        return self.name
    def set_name(self, newName):
        self.name = newName
    def get_model(self):
        return self.model
    def set_model(self, newModel):
        self.model = newModel
    def get_all(self):
        d = str(self.name)
        e = str(self.model)
        f = "The name of the bus is:  " + d + " and the model of the bus is : " + e
        return f
    def set_all(self, newName, newModel):
        self.name = newName
        self.model = newModel

#creation of bus object and function testing.       
bus1 = bus("A95","SomeModel")

bus1.set_all("B66", "DEEZUL")
bus1.get_all()