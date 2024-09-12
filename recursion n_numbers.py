def n_numbers(n,a=1):
    if a>n:
        return
    print(a)
    n_numbers(n,a+1)
n_numbers(10)