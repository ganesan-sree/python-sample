'''
Created on Apr 4, 2017

@author: 390607
'''

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.==%s" % self.variable)

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then pring out both values
print(myobjectx.variable)
print(myobjecty.variable)

myobjectx.function()        