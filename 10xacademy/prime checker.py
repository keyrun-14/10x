def is_prime(number):
    if number==1:
        return False
    elif number==2:
        return True
    elif number>2:
        for i in range(2,number):
            if number%i==0:
                return False
                break
        else:
            return True
n=int(input())
print(is_prime(n))
