from typing import List
from math import gcd
def add_frac(a:List[int],b:List[int]):
    denom= a[1]*b[1]// gcd(a[1],b[1])
    num= ((denom/a[1])*a[0]) + ((denom/b[1])*b[0])
    common_factor= gcd(num,gcd(a[1],b[1]))
    denom//=common_factor
    num//=common_factor
    add= [num,denom]
    print(add)


add_frac([1,3],[3,9])

