def print_times_table(n:int):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def print_times_table_with_recurrsion(n,i):
    print(f"{n} x {i}= {n*i}")
    i+=1
    if(i <= 10):
        print_times_table_with_recurrsion(n,i)
   

if __name__ == "__main__":
# print_times_table(5)
    print_times_table_with_recurrsion(5,1)