# https://github.com/splashoui/

# https://projecteuler.net/problem=49

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

from itertools import permutations

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

# create the number

def create(b):
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            difference = b[j] - b[i]
            if b[j] + difference in b:
                return str(b[i])+str(b[j])+str(b[j]+difference)
    return False

#sieving prime numbers upto 9999

primes = sieve(9999)

primes = [x for x in primes if x > 1487]

for num in primes:
    p = permutations(str(num))
    a = [int("".join(x)) for x in p]
    a = list(set([y for y in a if y in primes]))
    a.sort()
    if len(a) >= 3:
        if create(a):
            print(f"Answer is {create(a)}.")
            break
            


# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")   
