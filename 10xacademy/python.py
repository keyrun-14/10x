# # n=int(input())
# # arr=[]
# # for i in range(n):
# #     s=[]
# #     s.append(input())
# #     s.append(float(input()))
# #     arr.append(s)
# # sorted_arr=sorted(arr, key=lambda x: x[1])
# # print(arr)
# # print(sorted_arr)
# n= int(input())
# for i in range(n):
#     string=f'{n}-'
#     string1=""
#     for j in range(i):
#         string+=f'{n-(j+1)}-'        
#     for k in range(i):
#         string1+=f'-{(n-(k))}'
#     string1=string1[:0:-1]        
#     print("-"*((2*(n-i)-2))+string+string1+"-"*((2*(n-i)-2)))
# for i in range(n-2,-1,-1):
#     string=f'{n}-'
#     string1=""
#     for j in range(i):
#         string+=f'{n-(j+1)}-'
#     for k in range(i):
#         string1+=f'-{(n-(k))}'
#     string1=string1[:0:-1]        
#     print("-"*((2*(n-i)-2))+string+string1+"-"*((2*(n-i)-2)))

# def findCombinations(keypad, keys, combinations, index, result=''):
#     # if we have processed every digit of the key, print the result
#     if index == -1:
#         combinations.add(result)
#         return
 
#     # stores the current digit
#     digit = keys[index]
 
#     # get the size of the list corresponding to the current digit
#     length = len(keypad[digit])
 
#     # one by one, replace the digit with each character in the corresponding
#     # list and recur for the next digit
#     for i in range(length):
#         findCombinations(keypad, keys, combinations, index - 1, keypad[digit][i] + result)
 
 
# def findAllCombinations(keypad, keys):
 
#     # invalid input - return empty set
#     if not keypad or not keys:
#         return set()
 
#     # set to store all combinations
#     combinations = set()
 
#     # find and return all combinations
#     findCombinations(keypad, keys, combinations, len(keys) - 1)
#     return combinations
 
 


# # mobile keypad
# keypad = {
#     # 0 and 1 digit don't have any characters associated
#     2: ['A', 'B', 'C'],
#     3: ['D', 'E', 'F'],
#     4: ['G', 'H', 'I'],
#     5: ['J', 'K', 'L'],
#     6: ['M', 'N', 'O'],
#     7: ['P', 'Q', 'R', 'S'],
#     8: ['T', 'U', 'V'],
#     9: ['W', 'X', 'Y', 'Z']
# }

# # input number in the form of a list (number cannot start from 0 or 1)
# keys = [2, 3, 4]

# # find all combinations
# combinations = findAllCombinations(keypad, keys)
# print(combinations)


# def keypad_words(number):
#     keys=list(number)
#     keypad = {
#         2: ['A', 'B', 'C'],
#         3: ['D', 'E', 'F'],
#         4: ['G', 'H', 'I'],
#         5: ['J', 'K', 'L'],
#         6: ['M', 'N', 'O'],
#         7: ['P', 'Q', 'R', 'S'],
#         8: ['T', 'U', 'V'],
#         9: ['W', 'X', 'Y', 'Z']
#     }
#     def findCombinations(keypad, keys, combinations, index, result=''):
#         if index == -1:
#             combinations.add(result)
#             return
#         digit = keys[index]
#         length = len(keypad[digit])
#         for i in range(length):
#             findCombinations(keypad, keys, combinations, index - 1, keypad[digit][i] + result)
#     def findAllCombinations(keypad, keys):
#         if not keypad or not keys:
#             return set()
#         combinations = set()
#         findCombinations(keypad, keys, combinations, len(keys) - 1)
#         return combinations

    
#     combinations = findAllCombinations(keypad, keys)
#     print(sorted(combinations))
#     # print(list("234"))
# number = "234"
# keypad_words(number)

# Computes the next lexicographical permutation of the specified
# list in place, returning whether a next permutation existed.
# (Returns False when the argument is already the last possible
# permutation.)
# 
def next_permutation(array):
    l = len(array) - 1
    while l > 0 and array[l - 1] <= array[l]:
        l -= 1
    if l <= 0:
        return False
    j = l - 1
    while array[j+1] <= array[l - 1]:
        j += 1
    array[l - 1], array[j] = array[j], array[l - 1]
    array[l: ] = array[len(array)-1 : l-1 : -1]
    return array
print(next_permutation([2,1,3]))
# Example:
#   arr = [0, 1, 0]
#   next_permutation(arr)  (returns True)
#   arr has been modified to be [1, 0, 0]