# https://github.com/splashoui/

# https://projecteuler.net/problem=6

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# This is a simple problem, so we can solve this straightforward with a for loop operation.

# define the starting point of the numbers.
num_total, sum_sq = 0 , 0 

for num in list(range(1,101)):
    # The sum of the squares of the first hundred numbers
    sum_sq = sum_sq + num**2
    # The sum of the first hundred numbers
    num_total = num_total  + num
    
print(abs(sum_sq - num_total**2))

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
# Execution time: 0.00016927719116210938 
