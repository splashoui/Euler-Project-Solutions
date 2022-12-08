# https://github.com/splashoui/

# https://projecteuler.net/problem=9

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Creating two loops for number 1 and 2.

# We implement the given conditions and print the product if the conditions are met.

import math

number_list = list(range(1,1000))

for n1 in number_list:
    for n2 in number_list:
        n3 = n1 ** 2 + n2 ** 2 
        if n1  + n2 + math.sqrt(n3) == 1000:
            output = int(n1*n2* math.sqrt(n3))
print(output)  

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
