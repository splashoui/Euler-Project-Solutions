# https://github.com/splashoui/

# https://projecteuler.net/problem=9

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Creating two loops for number a and b.

# We implement the given conditions and print the product if the conditions are met.

for a in range(1,1000):
    for b in range(1,1000):
        if a + b <= 1000 and a < b < (1000-a-b) and a**2 + b**2 == (1000-a-b)**2:
                print(f"Answer is {a * b * (1000-a-b)}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
