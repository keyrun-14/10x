

# 1 1 0 0 0(0,4)
# 0 1 0 0 1(1,4) (1,5)
# 1 0 0 1 1(2,4)
# 0 1 0 1 0
# 1 0 1 0 1 (4,4) (rows, cols)


# (x-1,y-1)     (x-1,y)   (x-1,y+1)
# (x,y-1)        (x,y)     (x,y+1)
# (x+1,y-1)     (x+1,y)  (x+1, y+1)
input_array = [[0,0, 0, 0, 0], [0,0, 0, 0, 0], [0,0, 0, 0, 0], [0,0, 0, 0, 0], [0,0, 0, 0, 0]]

# At every step of solving problem you are doing something repetive..!!

# 1 1 0 0 0
# 0 1 0 0 1
# 1 0 0 1 1 
# 0 0 0 0 0
# 1 0 1 0 1

def find_islands(x, y):
    if (x < 0 or y < 0 or x > (rows-1) or y > (cols-1)): # valid poistion or not.
        return

    if (input_array[x][y] == 0):
        return
    
    input_array[x][y] = 0

    # This function should start doing our traversal logic..
    # let's check all neighbours. (0, 0)
    # x,y ... 8... (x-1, y-1) , (x+1, y+1) ) => 
    find_islands(x-1, y-1) 
    find_islands(x-1, y)
    find_islands(x-1, y+1)
    find_islands(x, y-1)
    find_islands(x,y+1)
    find_islands(x+1,y-1)
    find_islands(x+1,y)
    find_islands(x+1, y+1)



rows = len(input_array)
cols = len(input_array[0])
number_of_islands = 0
## 2D Array traversal
for i in range(0, rows):
    for j in range(0, cols):
        if input_array[i][j] == 1:
            # If we find "1" we wanted to run our find_islands logic starting from this 1 ?
            find_islands(i, j)
            number_of_islands = number_of_islands + 1

print("number of islands :: " + str(number_of_islands))
