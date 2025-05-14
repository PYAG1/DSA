def pair_CubeCount(n):
    count=0
    for i in range (1,n+1):
        for j in range(n+1):
            if i**3 + 2**j == n:
                count+=1
    return count


print(pair_CubeCount(9))
