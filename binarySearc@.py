### array should be [1,2,3,4,5,6,7]

def binarySearh(array,query):
    low,high=0, len(array)-1

 
    while low<=high:
        midd= (low+high)//2
        mid_num= array[midd]
        print("lo:",low,"high:",high,"mid",midd,"midnum:",mid_num)
        if mid_num == query:
            return midd
        elif mid_num < query:
            high=mid_num-1
        elif mid_num > query:
            low=mid_num + 1
    return -1

print(binarySearh([1,2,3,4,5,6,7],7))

