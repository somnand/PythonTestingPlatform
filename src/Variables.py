#Strings
str = "Hello World"
print(str.upper())

#Complex Numbers
a = 7+8j
b=4+7j
print("Complex addition " + (a+b).__str__())

#Collections
list=["apple","banana"]
print(list)
tuple=("apple","banana")
print(tuple)
range=range(3)
print(range)
set = {1,2,2,3}
print(set)

#Boolean
boolean = True
print("Boolean : "+boolean.__str__())

#Binary Datatypes
str_bytes = b"Hello World"
print(str_bytes)

barray = bytearray(5)
print(barray)
memview = memoryview(bytes(5))
print(memview)
