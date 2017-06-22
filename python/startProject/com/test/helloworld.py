'''
Created on Mar 20, 2017

@author: 390607
'''
print("This line will be printed.")

x = 1
if x == 1:
    # indented four spaces
    print("Ganesan \n x is 1.")
    
print("Goodbye, World!")

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)


mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)



one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a,b)


# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

print("Start testing:\n\n")

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    
    
mylist = [1,2,3]
print(mylist[3])