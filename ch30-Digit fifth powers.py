# https://github.com/splashoui/

# https://projecteuler.net/problem=30

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

tot = 0 
l = []
for num in range (2,5*9**5+1):
    if sum([int(x)**5 for x in str(num)]) == num:
        tot += num

print(f"Answer is {tot}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
