'''
Created on May 17, 2017

@author: 390607
'''

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
        if word != "the":
            word_lengths.append(len(word))
print(words)


##List comprehnsion for loop can be handle in same line code

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]

print(words)

print(word_lengths)




numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print("\n\nPostive number only =", newlist)

a= numbers[1]
print("first number only = %s" % a)
