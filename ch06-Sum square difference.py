# https://github.com/splashoui/

# https://projecteuler.net/problem=6

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# This is a simple problem, so we can solve this straightforward with 2 for loop operations.

# The sum of the squares of the first hundred numbers

a = sum([i**2 for i in range(0,101)])

# The square of the sum of the first hundred numbers

b = sum([i for i in range(0,101)])**2

print(f"The difference between the sum of the squares of the first hundred numbers ")
print(f"and the square of the sum is {b-a}")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
