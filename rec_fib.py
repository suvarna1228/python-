def recursivefib(n):
    if n<2 :
        return n
    return recursivefib(n-1) + recursivefib(n-2)


print(recursivefib(2)) 
print(recursivefib(4)) 