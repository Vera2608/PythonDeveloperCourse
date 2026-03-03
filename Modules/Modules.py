import math
import random

print(math.sqrt(25))

# for i in range(10): #print 10x
#     print(random.randint(1, 10)) #print een random interger tussen 1 en 10

def dobbelsteen():
    return random.randint(1, 6)

# voorbeeld
print(f"Je gooit: {dobbelsteen()}")

import datetime as dt

print(dt.datetime.now())

#print formatted datetime
print(dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

#print day of the week
print(dt.datetime.now().strftime("%A"))

#print the milliseconds of today
print(dt.datetime.now().strftime("%f"))
