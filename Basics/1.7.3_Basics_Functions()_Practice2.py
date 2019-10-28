# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:15:44 2019

@author: Yusef Quinlan
"""


def List_half_quart(num1,num2):   #This function shows we can return a list
    NumList = []
    NumList.append(float(num1))
    NumList.append(float(num2))
    NumList.append(float(num1) / 2)
    NumList.append(float(num2) / 2)
    NumList.append(float(num1) / 4)
    NumList.append(float(num2)/ 4)
    return NumList
    
NuevoList = List_half_quart(3,8)     #testing code

def CorporateSalesResponse(name, purchase_value, corpName):   #Function depicting automated response
    print("Dear " + name + " we at " + corpName + " are very happy for your purchase!")
    print("We are glad you have decided to make a purchase to the value of " + str(purchase_value))
    print("Please do not hesitate to purchase from us again!")
    
CorporateSalesResponse("Mr.Quinlan", 120, "Happy_inc")    #testing code

def Math1(num1,num2,num3):      #Function depicting a semi-complex mathematical calculation.
    num4 = num1 + num2 + num3
    num5 = num4 / num3
    num6 = num2 * num2 
    num7 = num6 + num5 + num4
    return num7

Math1(3,5,7)
Math1(6,92,12)
