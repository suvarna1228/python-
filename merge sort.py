def mergesort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=mergesort(a[:mid])
    right=mergesort(a[mid:])
    return merge(left,right)
def merge(left,right):
    merged=[]
    i=j=0
    while i< len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

a = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = mergesort(a)
print("Sorted array:", sorted_arr)