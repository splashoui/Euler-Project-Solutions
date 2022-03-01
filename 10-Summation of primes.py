# https://github.com/splashoui/

# https://projecteuler.net/problem=10

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print(f"Answer is {sumPrimes(2000000)}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
