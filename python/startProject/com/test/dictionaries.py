'''
Created on May 17, 2017

@author: 390607
'''
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
    # testing code
if "Jack" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill222" not in phonebook:
    print("Jill is not listed in the phonebook.")
    
    
del phonebook["John"]
print(phonebook)

phonebook.pop("Jack")
print(phonebook)    