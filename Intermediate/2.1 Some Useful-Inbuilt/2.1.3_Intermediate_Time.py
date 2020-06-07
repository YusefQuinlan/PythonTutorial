# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:49:20 2019

@author: Yusef Quinlan
"""

"""
 Looping a process, because modern computers are so fast the loop is completed
 almost instantly, in a real industrial process we might want to press material
 once a second rather than 25 times instantly.... normal loops do not allow this.
"""
for i in range(0, 25):
    print("Process in progress!")
   
"""By importing the time module, the time.sleep() function can be used. As an 
 argument an amount of seconds is used, and the sleep() function makes a delay
 equal to the argument specified; i.e. 1 would produce a 1 second delay.  
"""  
import time
for i in range(0, 25):
    time.sleep(1)
    print("Pressing some material!!!")
    
for i in range(0, 30):
    time.sleep(0.5)
    print("Do an action in game!")
    
for i in range(0,2):
    time.sleep(4)
    print("An action!")

"""Time can also be used to display the date-time using asctime() and also the
amount of seconds that have passed since 1 January 1970 at midnight (Unix time)
. Whilst this seems useless in itself, it can be used to find out how many
seconds have passed since the start of a process/loop to a particular point in
time. I.e. perhaps how long it took to run a for loop in its entirety or an update
on how long an industrial process has been running since it started at several intervals.
For example every 2 seconds the machine updates the time it has been running for.
""" 
print(time.asctime())

time.time()

ftime = time.time()
for i in range(0,5):
    time.sleep(2)
    print("the amount of seconds that have passed are: " + str(time.time() - ftime))
    
#The above comparison has been done by setting a base time into a variable 'ftime'
# and by comparing that to time.time() at the end of each iteration of the loop.