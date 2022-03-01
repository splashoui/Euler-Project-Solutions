# https://github.com/splashoui/

# https://projecteuler.net/problem=56

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# With 2 for loops, we iterave over all possible number combinations where a, b < 100.

l = []

for a in range(1,100):
    for b in range(1,100):
        # We do a**b operation and summing the digits of each result.

        # We are adding them to a list 

        l.append(sum(int(digit) for digit in str(a**b)))

# and taking the max value of the list to get the answer.
        
print(f"Answer is {max(l)}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
