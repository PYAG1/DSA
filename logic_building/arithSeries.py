def find_nth_term(a1,a2,n):
    diff = a2-a1
    result=a1
    for _ in range(1,n):
       result+=diff
    print(result)


find_nth_term(1,3,10)