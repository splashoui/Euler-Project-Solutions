# https://github.com/splashoui/

# https://projecteuler.net/problem=33

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

import numpy as np

from fractions import Fraction
import math

def remove(string, i): 
   a = string[ : i]
   b = string[i + 1: ]
   return a + b

product = 1

for x in range(10,100):
    for y in range(10,100):
        a=1
        if x < y:
            common=list(set(str(x)).intersection(set(str(y))))
            if common != []:
                res1 = int(remove(str(x),str(x).index(common[0])))
                res2 = int(remove(str(y),str(y).index(common[0])))
                try:
                    if x/y == res1/res2 and (str(x)[1] or str(x)[0]) != "0":
                        product *= Fraction(x,y)
                             
                except:
                    pass
                
print(f"Answer is {product.denominator}.")


# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Time: {end - start}")   
