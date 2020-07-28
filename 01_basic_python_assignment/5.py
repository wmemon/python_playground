def print_triangular_number(n):
    for num in range(1,n+1):
        print(f"{num}    {num * (num + 1) / 2}")
        print()
    return None

print_triangular_number(5)