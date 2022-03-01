# https://github.com/splashoui/

# https://projecteuler.net/problem=37

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

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


l = []
for num in primes:
    if len(str(num)) ==1: continue
    if all(int((str(num)[i:len(str(num))])) in primes and int((str(num)[0:i+1])) in primes for i in range(len(str(num)))):
        l.append(num)

print(f"Answer is {sum(l)}.")        
# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Time: {end - start}")   
