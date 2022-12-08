# https://github.com/splashoui/

# https://projecteuler.net/problem=4

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# My approach is to start the loops reversed which is from 999 until 100 and print the number if we find it.

# Since we are looking for the largest number, we can earn time by looking from highest to lowest.

# Firstly, storing two 3-digit numbers and storing it in list "num_list".

# Secondly, storing the multiplications of all 3 digit numbers in "multiplications"

# Thirdly, sorting the results of multipicilation from highest to lowest.

# With for loop, taking each number and with if condition we are checking

# If first 3 strings are equal to reversed version of last 3 strings printing the output and breaking the loop.

num_list = list(range(999,99,-1))

multiplications = []
for n1 in num_list:
    for n2 in num_list:
        multiplications.append(n1 * n2)
        
for mult in sorted(multiplications,reverse=True):
    if str(mult)[0:3] == str(mult)[-1:2:-1]:
        print(mult)
        break
    
# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   

# Execution time: 0.14335203170776367 
