import math
import random
"""
Multi-line comments; useful for long descriptions or functions documentation.
Unit 5: Comments & built-in libararies (packages or modules)
built-in libararies: math / random / datetime / od etc..
"""

# 3.141592653589793
print(f"PI = {math.pi}") 

# generate one random number between 1 and 100
n = random.randint(1, 100)
print("Random generated Number between 1 and 100 using randit(): ",n)

# generate 10 random numbers between between 1 and 100
 # and calculate their square roots
 #store all the numbers in a list
numbers = [] # empty list
numbers_square_roots = [] # will contain the squre roots of numbers
for i in range(10):
    n= random.randint(1, 100)
    s = round(math.sqrt(n),2)
    numbers.append(n)
    numbers_square_roots.append(s)
    print(f"n = {n}, sqrt(n) = {s}")


 # print both lists

print("\n\nList of all the Random generated Numbers:")
print(numbers)
print("List of Squareroot of Random generated Numbers:")
print (numbers_square_roots)

print("\n Program Ended!!!")
