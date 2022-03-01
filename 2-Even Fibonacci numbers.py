#https://github.com/splashoui/

# https://projecteuler.net/problem=2

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Creating previous and current values as start point.
# Creating while loop until the current number is 4 million as the condition given in the problem.
# Applying the condition to find even valued numbers and summing them.

previous, current = 0, 1
total = 0
while True:
    previous, current  = current , previous + current
    if current >= 4000000:
        break
    elif current % 2 == 0:
        total += current

print(f"Answer is {total}.")


# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start}.")   
