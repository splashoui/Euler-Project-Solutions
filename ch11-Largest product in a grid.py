# https://github.com/splashoui/

# https://projecteuler.net/problem=11

#****************************************Approach*********************************

# Firstly, to get the 20x20 grid, I have saved the grid in txt file in my local file.
# Later on, I will read the data from txt file. 

# I will convert the data into a 20x20 Matrix to be able

# to access to the numbers with their positions easily. 

# Reading the data and converting to a matrix to be able to access to the positions.

with open('matrix.txt') as f:
    grid_data = [i.split() for i in f.readlines()]

# I will check 3 possibilites:

#                       ""ROW WISE CALCULATIONS""
# Horizontally from left to right which is the same thing as from right to left.

#                     ""COLUMN WISE CALCULATIONS""
# Vertically from top to bottom which is the same thing as from bottom to top.


#                      ""DIAGONAL CALCULATIONS""

# ** From left to right diagonally and from right to left diagonally. 
# To do the one with from right to left diagonally, I have reversed the matrix vertically.



# ""ROW WISE CALCULATIONS""

dic2 = {}
for i in range(17):
    for j in range(20):
        a = int(grid_data[j][i])*int(grid_data[j][i+1])*int(grid_data[j][i+2])*int(grid_data[j][i+3])
        b = [[j,i],[j,i+1],[j,i+2],[j,i+3]]
        dic2[str(b)] = a
        
max_value2 = max(dic2.values())  # maximum value
max_keys = [k for k, v in dic2.items() if v == max_value2] # getting all keys containing the `maximum`

print(f"Row wise calculation: {max_value2} , {max_keys}")


# ""COLUMN WISE CALCULATIONS""

dic3 = {}
for i in range(20):
    for j in range(17):
        a = int(grid_data[j][i])*int(grid_data[j+1][i])*int(grid_data[j+2][i])*int(grid_data[j+3][i])
        b = [[j,i],[j+1,i],[j+2,i],[j+3,i]]
        dic3[str(b)] = a
        

max_value3 = max(dic3.values())  # maximum value
max_keys = [k for k, v in dic3.items() if v == max_value3] # getting all keys containing the `maximum`

print(f"Column wise calculation: {max_value3} , {max_keys}")


# ""DIAGONAL CALCULATIONS"".

# Normal matrix

dic1 = {}
for i in range(17):
    for j in range(17):
        a = int(grid_data[j][i])*int(grid_data[j+1][i+1])*int(grid_data[j+2][i+2])*int(grid_data[j+3][i+3])
        b = [[j,i],[j+1,i+1],[j+2,i+2],[j+3,i+3]]
        dic1[str(b)] = a
        
        
max_value1 = max(dic1.values())  # maximum value
max_keys = [k for k, v in dic1.items() if v == max_value1] # getting all keys containing the `maximum`

print(f"Diagonal normal matrix: {max_value1} , {max_keys}")


# Reversed matrix

# To do that, I have used numpy library to reverse my matrix vertically.
# index = 1 vertically, index = 0 horizontally.

import numpy as np

myl_flip_v = np.flip(grid_data,1)

dic4 = {}
for i in range(17):
    for j in range(17):
        a = int(myl_flip_v[j][i])*int(myl_flip_v[j+1][i+1])*int(myl_flip_v[j+2][i+2])*int(myl_flip_v[j+3][i+3])
        b = [[j,i],[j+1,i+1],[j+2,i+2],[j+3,i+3]]
        dic4[str(b)] = a
      
    
max_value4 = max(dic4.values())  # maximum value
max_keys = [k for k, v in dic4.items() if v == max_value4] # getting all keys containing the `maximum`

print(f"Diagonal reversed matrix: {max_value4} , {max_keys}")

print(f"Max value is {max(max_value1,max_value2,max_value3,max_value4)}")
