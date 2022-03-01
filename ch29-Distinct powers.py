# https://github.com/splashoui/

# https://projecteuler.net/problem=29


# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Created an empty set since we do not want to store repeated values.

res = set()

# Using two for loops between 2,100 for a and b to calculate a**b 

# to find the numbers of the distinct terms.

for a in range(2,101):
    for b in range(2,101):
        res.add(a**b)

print(len(res))


# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
