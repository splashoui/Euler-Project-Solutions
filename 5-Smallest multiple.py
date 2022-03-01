# https://github.com/splashoui/

# https://projecteuler.net/problem=5

import time

start = time.time()

# In this problem, my approach is to take off the common divider numbers like 2,3,4,5,6,7,8,,9,10,12,15 in the range 1,20.

# Since the minimum integer is given as 2520, we can start from 2520 and increase our range with 2520.

# Then with if condition we can divide the numbers with list of dividors.


divider_list = [11, 13, 14, 16, 17, 18, 19, 20]

for num in range(2520, 999999999, 2520):
    if all(num % n == 0 for n in divider_list):
        print(f"Answer is {num}.")
        break
            
end = time.time()

print(f"Execution time: {end - start} ")