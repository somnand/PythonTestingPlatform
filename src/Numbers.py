#Contains User Inputs and numbers
from math import *

x = input("Enter value of x ")
y = input("Enter value of y ")
decimal = input("Enter a decimal number : ") 

print("Product = "+str(int(x)*int(y)))#To print messages with number encapsulate the numbers within the function str()
print("Product = "+(int(x)*int(y)).__str__())#This also works the same as above
#Maths functions
print("Floor value : "+str(floor(float(decimal))))
print("Ceiling value : "+str(ceil(float(decimal))))
print("Round value : "+str(round(float(decimal))))
