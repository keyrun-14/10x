# 1 2 3 4
# 3 2 5 7
# 9 8 7 6
# 1 10 11 12

# Matrix will contain only elements from 0 to 20
# 0 1 2 3 4 5 6 7 .... 20

# [ a1  a2 a3 a4 a5 a6 ...... a20]
# a[0]

# a[9]

# a[19]
# [2 0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0]
#   a[e] = a[e] + 1

# You need to find the unique elemets in the matrix or 2D array..

# 10, 5, 11, 4 8

# count of elements...?
# how are we going to track the count..?


# [ 0    1 2   3   4 5 ......  19 20]
# [ 1 ........ ]

row = int(input())
col = int(input())

matrix = []
counts_array = []

# [[] [] [] [] [] ]
# 1 2 3 4
# 3 2 5 7
# 9 8 7 6
# 1 10 11 12

# # [ [] ] => 1*3
# for i in range(row):
#     matrix.append([]) # Added one row.. is ultimately list..?
#     for j in range(col):
#         matrix[i].append(int(input()))
#         # matrix[i][j] = int(input())

for i in range(row):
    single_row = [int(x) for x in input().split()]
    matrix.append(single_row)

print(matrix)

for i in range(21):
    counts_array.append(0)

for i in range(row):
    for j in range(col):
        index = matrix[i][j]
        counts_array[index] += 1

print(counts_array)
for i in range(21):
    if (counts_array[i] != 0):
        print("count of " + str(i) + " is :: " + str(counts_array[i])) 

# TC : m*n
# SC :: O(21) => O(1)

# [[1, 2, 3], [1, 2, 3], [4, 6, 6]]
# [0, 2, 2, 2, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]