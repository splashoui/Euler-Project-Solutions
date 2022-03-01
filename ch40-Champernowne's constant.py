# https://github.com/splashoui/

# https://projecteuler.net/problem=40

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Using loop to create numbers and adding them as digits horizontally by converting them to string.

l = []
for i in range(1,200000):
    l.append(str(i))

# After storing them in a list, we need to join them to make one string.

decimal = ''.join(l)

# Now we have a single line string like "11111111111111111111111111111111111"

# which we can access to each nth position and multiply the asked nth digits.

result = int(decimal[0])*int(decimal[9])*int(decimal[99])*int(decimal[999])*int(decimal[9999])*int(decimal[99999])*int(decimal[999999])

print(f"Answer is {result}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
