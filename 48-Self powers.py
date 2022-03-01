# https://github.com/splashoui/

# https://projecteuler.net/problem=48

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Using simple for loop to iterate between 1,1001 and summing squares of the numbers.

# and selecting the last ten digits by reverse indexing by [-10:].

result = str(sum([i**i for i in range(1,1001)]))[-10:]

print(f"Answer is {result}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
