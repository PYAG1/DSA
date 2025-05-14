def reverse_String(n):
    digit_reversed_string=""
    while n > 0:
        digit_reversed_string += str(n % 10)
        n //= 10
    return digit_reversed_string

print(reverse_String(12345))