def binarySerach(list1,query): ###use on a sorted list
    low,high = 0,len(list1)-1
    midnum = (low + high)//2
    if list1[midnum] == query:
        return midnum
        
    elif list1[midnum] < query:
        position = low
        while position < midnum:
            if list1[position] == query:
                return position
            position +=1
    
    elif list1[midnum] > query:
        position = midnum+1
        while position > midnum:
            if list1[position] == query:
                return position
            position +=1
    
    return -1
    

            
def binarySerach2(list1,query): ###use on a sorted list
    low,high = 0,len(list1)-1
    while low <= high:
        mid = (low + high)//2
        midnum = list1[mid]

        print("lo:",low,"high:",high,"mid",mid,"midnum:",midnum)
        if midnum == query:
            return mid
        elif midnum < query:
            high= mid -1
        elif midnum > query:
            low = mid+1
    return -1
        
 
    



print(binarySerach2([5,4,3,2,1,9,0,99],99))