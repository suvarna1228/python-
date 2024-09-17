def eelement(a):
    if len(a)<2:
        return None
    largest=a[0]
    second=float('-inf')
    for i in range(1,len(a)) :
       if a[i]>largest:
           largest=a[i]
    for i in range(len(a)):
        if a[i] != largest and a[i] > second:
            second = a[i]
    return second if second != float('-inf') else None
a=[34,54,67,89,2,45,]
print("the second largest no is:",eelement(a))