def find_natural_number_sum(n):
    _sum = 0
    for i in range(n+1):
        _sum+=i
    print(_sum)


if __name__ == "__main__":
# print_times_table(5)
    find_natural_number_sum(5)