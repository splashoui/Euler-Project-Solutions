# https://github.com/splashoui/

# https://projecteuler.net/problem=34

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

from math import factorial 

# Creating a function passing a number, iterating over each digit of the number.

# Taking the factorial of each digit and summing them.

# Checking the condition if the number is equal to the sum of the digits' factorial.

def fact(n):
    summ= 0
    for i in range(0,len(str(n))):
        summ += factorial(int(str(n)[i]))
        if summ == n:
            return summ
        else: 
            pass

# We are iterating over range(3,100000) and summing them if the conditions are met.

# If fact(i) is None: pass, is to avoid empty results.

tot = 0 
for i in range(3,100000):
    if fact(i) is None:
        pass
    else:
        tot += fact(i)
    
print(f"Answer is {tot}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   

