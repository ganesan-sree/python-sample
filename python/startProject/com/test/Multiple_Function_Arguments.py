'''
Created on May 17, 2017

@author: 390607
'''
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))
    #print("And all the rest... %s" % therest)
    
    
foo("a","b","c","d")    

foo("a","b","c","d","e","f")


def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("\n\n\nThe sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))








# edit the functions prototype and implementation
def foo1(a, b, c, *args):
    return len(args)

def bar1(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo1(1,2,3,4) == 1:
    print("\n\nGood.")
if foo1(1,2,3,4,5) == 2:
    print("Better.")
if bar1(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar1(1,2,3,magicnumber = 7) == True:
    print("Awesome!")