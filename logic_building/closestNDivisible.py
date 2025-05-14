def closet_and_disible(n, m):
    rem = n // m
    
    # Closest multiple below or equal to n
    first_closest = m * rem
    
    # Closest multiple above n
    if n * m > 0:
        upper = m * (rem + 1)
    else:
        upper = m * (rem - 1)
    
    # Compare distances to find the closest one, with a preference for higher absolute value
    if abs(n - first_closest) < abs(n - upper):
        closest = first_closest
    elif abs(n - first_closest) > abs(n - upper):
        closest = upper
    else:
        # If both are equally close, return the one with the higher absolute value
        closest = first_closest if abs(first_closest) > abs(upper) else upper
    
    print("Closest:", closest)

# Test case
closet_and_disible(14, 4)
