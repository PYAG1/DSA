def check_triangle_valid(a,b,c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return "Invalid"
    else:
        return "Valid"

print(check_triangle_valid(7,10,5))