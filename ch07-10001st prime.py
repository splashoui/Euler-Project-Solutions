# https://github.com/splashoui/

# https://projecteuler.net/problem=7

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

# I have decided to use the sieve of Eratosthenes algorithm for finding all prime numbers up to any given limit.

# This algorithm is one of the fastest way to generate prime numbers.

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    #even numbers except 2 have been eliminated
    for i in range(3,int(n**0.5+1),2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3,n,2):
        if is_prime[i]:
            prime.append(i)
    return prime

# Sieving prime numbers up to 1 million and picking the 10001th number.

print(f"Answer is {sieve(1000000)[10001]}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
