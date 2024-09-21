def Left_rotate(a ,d):
    n = len(a)
    d=d%n
    return a[d:]+a[:d]
a=[1,2,3,4,5,6]
d=2
result=Left_rotate(a,d)
print(result)