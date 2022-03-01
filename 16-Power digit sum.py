# https://github.com/splashoui/

# https://projecteuler.net/problem=16

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

res = 0 

# Looping the digits of the result of 2**1000.

# Summing them in the variable "res".

for i in str(2**1000):
    res += int(i)
    
print(f"Answer is {res}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   


