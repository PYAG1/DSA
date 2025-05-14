def find_sum_of_digits(n):
    _sum=0
    n_str= str(n)
    for i in n_str:
        _sum += int(i)
    print(_sum)

 


find_sum_of_digits(103)


def find_sum_of_digits(n):
    """
    Find the sum of the digits of an integer n.
    
    Args:
        n (int): The input integer.
    
    Returns:
        int: The sum of the digits of |n|. Returns -1 if n is not an integer.
    """
    if not isinstance(n, int):
        return -1  # Handle non-integer inputs
    n = abs(n)  # Handle negative numbers
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10  # Get the last digit
        n //= 10  # Remove the last digit
    return digit_sum