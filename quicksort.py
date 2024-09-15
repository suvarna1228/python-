def quicksort(a):
    if len(a)<2:
        return a
    else:
        pivot=a[len(a)-1]
        left=[]
        right=[]
        for i in range (len(a)-1):
            if a[i]< pivot:
                   left.append(a[i])
            else:
                 right.append(a[i])

        return quicksort(left)+[pivot]+quicksort(right)
a=[8,20,-2,4,-6]
print(quicksort(a))                   
    