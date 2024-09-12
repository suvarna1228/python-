def n_numbers(n):
    if n<1:
        return
    print(n)
    n_numbers(n-1)
n_numbers(10)