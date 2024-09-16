def Recursive_bubble_sort(a ,n=None):
    if n is None:
        n=len(a)
    if n==1:
        return
    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    Recursive_bubble_sort(a, n - 1)
a = [64, 34, 25, 12, 22, 11, 90]
Recursive_bubble_sort(a)
print(a)