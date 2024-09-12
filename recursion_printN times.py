def print_n(a,n):
    if n==0:
        return
    print(a)
    print_n(a,n-1)
print_n("hi",10)