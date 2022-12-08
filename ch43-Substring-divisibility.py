# https://github.com/splashoui/

# https://projecteuler.net/problem=43

# time module for calculating execution time
import time

# permutation package
from itertools import permutations

# time at the start of program execution
start = time.time()


# permutations of 0-9 pandigital
p = list(permutations('0123456789'))

list_of_numbers = []

for num in p:
    # Removing then numbers starting with 0.
    if (num[0] != '0') and \
        (int(''.join(num[1:4])) % 2 == 0) and \
        (int(''.join(num[2:5])) % 3 == 0) and \
        (int(''.join(num[3:6])) % 5 == 0) and \
        (int(''.join(num[4:7])) % 7 == 0) and \
            (int(''.join(num[5:8])) % 11 == 0) and \
            (int(''.join(num[6:9])) % 13 == 0) and \
            (int(''.join(num[7:10])) % 17 == 0):

        list_of_numbers.append(int(''.join(num)))

print(f'Answer is {sum(list_of_numbers)}')

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")

# Execution time: 1.6889405250549316
