#!/usr/bin/env python3

print('Hello World')
# Testing Git

# format function
x=43
print('Hello Wolrd {}'.format(x))

#f fucntion
x=43
print(f'Hello World {x}')

## if conditoin
x = 44
y = 33

if x < y:
    print(f'x < y: x is {x} and y is {y}')
else:
    print(f'x > y: x is {x} and y is {y}')
    
## while loop    
words = ('one' , 'two', 'three')
n=0
while(n < len(words)):
    print(words[n])
    n += 1
else:
    print('All elimented printed')
    
    
## Simple Fibonacci series

a, b = 0, 1
while b <1000:
    print(b, end = ' ', flush = True) # flush ==> flushes memory , end ==> change the endlines chars
    a, b = b, a + b

print()
 ## for loop

animals = ( 'bear' , 'lion' ,'elephant' ,'cat' )

for i in animals:
    if i == 'lion': continue
    print(f'Animal Listing: {i}')

# Animal Listing: bear
# Animal Listing: elephant
# Animal Listing: cat

## Functions
def function(n):
    print(f'Parsed Value {n}')
    
function(33)

# Parsed Value 33

## Find a prime numenr

def isprime(n):
    if n<=1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True
    
for n in range(100):
    if isprime(n):
        print(f'{n}', end = ' ')

print()
        
######## Class ##############3

class Duck:
    def quack(self): ## Methods have a self constructor where as functions does not
        print('Quaaak')
        
    def walk(self):
        print('Walks')
        
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    
print('Class')
print('=====')
if __name__ == '__main__': main() ## Good practice, this will interprite the entire program proir runing

        