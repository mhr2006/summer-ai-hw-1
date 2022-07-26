from math import pow, sqrt
from random import randint, shuffle, choice 

result_1 = pow(2,4)
print ("result_1 is", result_1)

result_2 = sqrt(16)
print ("result_2 is", result_2)

result_3 = randint(0,100)
print ("result_3 is", result_3)

names = ["Amaryllis","Godson","Emily","Reina","Derin","Elena","Inacio"]
print ("Original names: ", names)

shuffle(names)
print ("names after shuffle: ",names)

result_4 = choice(names)
print ("chosen name is: ",result_4)