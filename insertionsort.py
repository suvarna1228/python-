def selectionsort(a):
    n=len(a)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if a[j]<a[min_index]:
              min_index=j
        a[i],a[min_index]=a[min_index],a[i]
a=[8,28,-2,4,-6]
selectionsort(a)
print("sorted arrey :",a)