def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key <a[j]:
            a[j+1]=a[j]
            j-=1
            a[j+1]=key
a=[8,28,-2,4,-6]
insertion_sort(a)
print("sorted arrey :",a)