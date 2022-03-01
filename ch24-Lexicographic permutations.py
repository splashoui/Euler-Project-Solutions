# https://github.com/splashoui/

# https://projecteuler.net/problem=24


# time module for calculating execution time
import time
from itertools import permutations

# time at the start of program execution
start = time.time()

# Using the permutation library to create the permutations of '0123456789'.

# And printing the millionth value of the list and joining the list numbers with "".

print(f"Answer is {''.join(list(permutations('0123456789'))[999999])}")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   

