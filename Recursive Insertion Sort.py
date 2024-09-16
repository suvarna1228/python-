def recursive_insertion_sort(a,n=None):
    if n is None:
        n=len(a)
    if n<=1:
        return
    recursive_insertion_sort(a,n-1)
    last=a[n-1]
    j=n-2
    while j>= 0 and a[j]>last:
        a[j+1]=a[j]
        j-=1
        a[j+1]=last

a=[12,11,3,45,-1]
recursive_insertion_sort(a)
print(a)