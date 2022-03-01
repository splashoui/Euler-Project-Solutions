# https://github.com/splashoui/

# https://projecteuler.net/problem=45

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# Defining the rules for triangle, pentagonal and hexagonal functions.

def triangle(n):
    return n*(n+1)//2

def pentagonal(n):
    return n*(3*n-1)//2

def hexagonal(n):
    return n*(2*n-1)

# Creating main function to loop over numbers which will meet the condition.

# To find the next triangle number.

def main():
    p = set(pentagonal(n) for n in range(100000))
    h = set(hexagonal(n) for n in range(100000))
    for n in range(100000):
        t = triangle(n)
        if t in p and t in h and t > 40755:
            print(f"Answer is {t}.")
            
main()

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
