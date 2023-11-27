def print_odd_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} adalah angka genap.")
        else:
            print(f"{i} adalah angka ganjil.")

print_odd_even_numbers(10)

