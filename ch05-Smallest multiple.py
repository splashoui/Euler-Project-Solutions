# https://github.com/splashoui/

# https://projecteuler.net/problem=5

import time

start = time.time()

# In this problem, my approach is to take off the common divider numbers like 2,3,4,5,6,7,8,,9,10,12,15 in the range 1,20.

# Since the minimum integer is given as 2520, we can start from 2520 and increase our range with 2520.

# Then with if condition we can divide the numbers with list of dividors.


# define the range of numbers to check
numbers = range(1, 21)

# loop over the range of numbers
for num in list(range(2520, 999999999, 2520)):
    # check if the number is evenly divisible by all of the numbers from 1 to 20
    if all(num % n == 0 for n in numbers):
        # print the number and break out of the loop
        print(num)
        break
        
end = time.time()

print(f"Execution time: {end - start} ")
# Execution time: 1.4066696166992188e-05
