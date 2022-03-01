#https://github.com/splashoui/

# https://projecteuler.net/problem=1

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Creating an empty list, storing the values below 1000 which can be divided by 3 or 5  
# finding the sum of the values in the created list.  

lis = []
[lis.append(i) for i in list(range(1,1000)) if i % 3 ==0 or i % 5 ==0]

print(f"Answer is {sum(lis)}")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
