def find_prime(n):
    for i in range(2,n-1):
        if(n%i==0):
            return False
        else:
            return True
        


print(find_prime(10))