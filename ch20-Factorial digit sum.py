# https://github.com/splashoui/

# https://projecteuler.net/problem=20


# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

import math # math library to use factorial.

tot = 0

# Simple problem, simple solution, we have iterated on the calculation 100!

# We take each digit and sum them and get the answer.

for j in range(0,len(str(math.factorial(100)))):
    tot += int(str(math.factorial(100))[j])    

print(f"Answer is {tot}.")


# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start}") 
