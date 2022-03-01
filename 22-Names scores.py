# https://github.com/splashoui/

# https://projecteuler.net/problem=22

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

from string import ascii_uppercase

# In the score function:
# Using ascii_uppercase library to find the alphabetical value for each name.

def score(word):
    return sum(ascii_uppercase.index(c) + 1 for c in word.strip('"'))

# Reading the text file, splitting the names by coma and sorting them alphabetically.

with open('names.txt') as f:
  names = f.read().split(',')
  names.sort()

# Using the enumerate function, numbering the names to have rank order score 

# To multiply with the alphabetical value for each name

print(sum(i*score(x) for i, x in enumerate(names, 1)))


# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
