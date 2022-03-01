# https://github.com/splashoui/

# https://projecteuler.net/problem=17

## Approach ##

# Firstly, by using the library inflect, we are converting the numbers to 

# written out of words. Then, while adding them to a list;

# As being indicated in the note, we should remove spaces and hyphens. 

# I have removed the spaces by replace and the hyphens by using regex ""-\b|\b-""

# Which removes the hyphens between the string.


import time     # time module for calculating execution time
import inflect  # converts the numbers written out in words
import re   # library to use regex expressions

# time at the start of program execution
start = time.time()

p = inflect.engine()

l =[]
for i in range(1,1001):
    l.append(re.sub(r'-\b|\b-', '', p.number_to_words(i)).replace(" ",""))

# Counting the letters    

tot = 0
for w in l:
    tot += len(w)

print(f"Answer is {tot}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
