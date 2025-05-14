def return_possiblities(origin: int, target):
    var = list(str(origin))
    totalsum = 0
    product = 1
    array_result = []
    
    for i in var:
        totalsum += int(i)
        product *= int(i)
    
    if totalsum == target:
        array_result.append("+".join(var))
    
    if product == target:
        array_result.append("*".join(var))
    
    return array_result 
    
print(return_possiblities(3456237490, 9191))