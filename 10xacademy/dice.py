# your code goes here
'''
n=int(input())
if n==6:
	print("1")
elif n==5:
	print("2")
elif n==4:
	print("3")
elif n==3:
	print("4")
elif n==2:
	print("5")
elif n==1:
	print("6")
else:
    print("invalid input")
'''
#another method  using if else condition
topface=int(input())
bottomface=((topface+1)-topface)
if 1<=topface<=6:
	print(bottomface)
else:
	print("invalid input")