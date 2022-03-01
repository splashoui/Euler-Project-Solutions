# https://github.com/splashoui/

# https://projecteuler.net/problem=52

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Looping over range (1,1000000), creating lists of the digits of the 2x,3x,4x,5x,6x of the number.

for num in range(1,1000000):
    # Checking if the numbers have the same digits.
    if set(list(str(num))) == set(list(str(num*2)))==set(list(str(num*3))) == set(list(str(num*4)))== set(list(str(num*5))) == set(list(str(num*6))):
        # If the condition is met, we print the number.      
        print(f"Answer is {num}.")
        # We break the program, when we get the print.
        break

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start}")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start}")
