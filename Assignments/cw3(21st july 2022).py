import math as mymath
import random as myrandom

result_1 = mymath.pow(2,4)
print ("result_1 is", result_1)

result_2 = mymath.sqrt(16)
print ("result_2 is", result_2)

result_3 = myrandom.randint(0,100)
print ("result_3 is", result_3)

names = ["Amaryllis","Godson","Emily","Reina","Derin","Elena","Inacio"]
print ("Original names: ", names)

myrandom.shuffle(names)
print ("names after shuffle: ",names)

result_4 = myrandom.choice(names)
print ("chosen name is: ",result_4)