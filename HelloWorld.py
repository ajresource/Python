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

        
