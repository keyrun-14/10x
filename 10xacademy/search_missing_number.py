# arr=[1,2,3,4,5,7,8,9,10]
# b=arr[-1]*(arr[-1]+1)//2
# print(b)
# for i in range(1,5):
#     print('*'*i)

# def foo(l1, n):
#   z = []
#   for i in range(n):
#     z.append(l1[i])
#     z.append(l1[i+n])

#   return z 

# l1 = [2, 2, 4, 4, 2, 4, 2]
# n = 3
# if __name__ == "__main__": 
#   print(foo(l1, n))

# print("A"*"A")
# names = ['Rich', 'Mouse', 'Flower', 'Man']
# print(names[-1][-1])

# def func(x = 1, y = 2):
#   return x + y, x - y

# x, y = func(y = 2, x = 1)
# print(x, y)
# print(['love', 'python'][bool('cutshort')])
# print(0.7+0.2==0.9)
# a = [(lambda x: x * 2)(x) for x in range(5)] 
# print(a)
# print( 1 < "1" )
# print( 1 > "1" )
# print( 1 == "1" )
# print( 1 != "1")
# a,b,c=1,2,3
# a,b,c
# def my_func(s, z):
#   total = 0
#   len_str = len(s)

#   for x, y in z:
#     if x == 0:
#       total += y
#     else:
#       total -= y
#   print(total)
#   total = total % len_str
#   print(total)
#   print(s[total:] + s[:total])


# s = 'cutshort'
# z = [[0, 3], [1, 11]]

# if __name__ == "__main__":
#   my_func(s, z)


# val1=28**0
# val2=2.5
# val3='123'
# val4=int(val3)
# print(val1+val2+val4)


# def oddsums(n):
#   total=0
#   result=[]
#   for i in range(1,n+1):
#     odd= 2*i-1
#     total=total+odd
#     result.append(total)
#   return result


# def my_func(st):
#   l1 = [ch for ch in st if ch.isalpha()]
#   return ''.join(l1.pop() if ch.isalpha() else ch for ch in st)


# st = 'ab-cd-ef'
# print(my_func(st))

def my_func(num):
  data = [0]
  for i in range(1, num+1):
    data.append(data[i >> 1] + int(i & 1))
  return data


num = 6
print(my_func(num))