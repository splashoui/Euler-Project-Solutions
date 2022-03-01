# https://github.com/splashoui/

# https://projecteuler.net/problem=4

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# My approach is to start the loops reversed which is from 999 until 100 and print the number if we find it.

# Since we are looking for the largest number, we can earn time by looking from highest to lowest.

# Firstly, storing two 3-digit numbers and storing it in list "num".

# Secondly, sorting the results of multipicilation from highest to lowest.

# With for loop, taking each number and with if condition we are checking

# If first 3 strings are equal to reversed version of last 3 strings.

num=[]
for i in range(999,99,-1):
    for j in range(999,99,-1):
        num.append(i*j) 

for x in sorted(num,reverse=True):
    if (str(x)[0:int(len(str(x))/2)]) == (str(x)[-int(len(str(x))/2):][::-1]):
        print(x)
        break
    
# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
