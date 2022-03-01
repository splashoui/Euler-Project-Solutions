# https://github.com/splashoui/

# https://projecteuler.net/problem=3

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# My approach in this problem is dividing the number while the number is bigger than 1.

# Created an empty list to store prime divisors.

# Starting from the first prime number f = 2. Second while, checks if the number divisible by f.

# If f can divide the number, f is being added to our list, if not, we add +1 to f to try next divisor.

def prime_factor(num):
    factors = []
    f = 2
    while num > 1:
        while num % f == 0:
            num = num/f
            factors.append(f)
        f = f + 1
    return factors

print(f"Answer is {max(prime_factor(600851475143))}.")


# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
