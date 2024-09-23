def linear_search(a,num):
    n=len(a)
    for i in range(n):
        if a[i]==num:
           return i
    return -1

a=[1,3,5,6]
num=6
value= linear_search (a , num)
print(value)
