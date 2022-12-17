def reverse_string(s,l):
    if l==0:
        return ""   
    return s[l-1] + reverse_string(s,l-1)
for i in range(int(input())):
	s=input()
	l=len(s)
	print(reverse_string(s,l))
# def reverse_string(a, l):
#     if l < 0:
#         return ''
#     else:
#         return a[l] + reverse_string(a, l-1)
# for i in range(int(input())):
# 	a=input()
# 	print(reverse_string)

#    if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]

# def reverse_string(s):
# 	if s=='':
# 		return s
# 	r = reverse_string(s[1:])
# 	return r +  s[0]


# 1.
# s= 'hello'
# r=func('ello')
# r = 'olle'
# return 'olle'+'h' = 'olleh'

# 2.
# s='ello'
# r=func('llo')
# r = 'oll'
# return 'oll'+'e' = 'olle'

# 3.
# s='llo'
# r=func('lo')
# r='ol'
# return 'ol'+ 'l' = 'oll'

# 4.
# s='lo'
# r=func('o')
# r='o'
# return 'o'+'l' = 'ol'

# 5.
# s='o'
# r=func('')
# r=''
# return ''+'o' = 'o'

# 6.
# s=''
# return ''





# def reverse_string(s):

# 	if s=='':
# 		return s
	
# 	#return reverse_string(s[1:])+s[0]
# 	r = reverse_string(s[1:])
#     return r +  s[0]


# n=int(input())
# lst=[]
# for i in range(n):
# 	string=input()
#     lst.append(reverse_string(string))
# for str in lst:
#     print(str)