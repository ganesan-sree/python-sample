'''
Created on Apr 4, 2017

@author: 390607
'''


primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
  
    
    
print('\n\n\n')    
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)
print('\n\n') 
# Prints out 3,4,5
for x in range(3, 6):
    print(x)
print('\n\n') 
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
    
    
    
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1    
    
    
    
    
    
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# print('Prints out only odd numbers - 1,3,5,7,9')
print('Prints out only odd numbers - 1,3,5,7,9')
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)    