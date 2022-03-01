# https://github.com/splashoui/

# https://projecteuler.net/problem=25

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Creating previous and current variables to sum them to find the next fib number.

# Assigning start values for previous and current numbers and count variable.

prev, cur = 0, 1
count = 1
# Putting while loop with condition dıring our current number does not have 4 digits.

# We are adding "1" to our counter to find the index of our first 4 digit fib number.

while len(str(cur)) != 1000:
    prev, cur = cur, prev + cur
    count += 1

print(f"Answer is {count}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
