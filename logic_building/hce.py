
import math 
def find_hcf(a,b):
    lcm = (a*b)/math.gcd(a,b)
    return lcm

print(find_hcf(5,11))