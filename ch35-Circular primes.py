# https://github.com/splashoui/

# https://projecteuler.net/problem=35

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

#To create prime numbers up to 1 million.

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

#sieving prime numbers upto 1 million
primes = set(sieve(1000000))

# to rotate the digits of the number
def rotation(n):
    rotations = set()
    for i in range(len( str(n))):
        rotations.add(int( str(n)[i:] + str(n)[:i] ))
    return rotations

# to check if all the rotations are prime.
tot = 0
for num in primes:
    if rotation(num).issubset(primes):
        tot += 1

print(f"Answer is {tot}.")

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Time: {end - start}")   
