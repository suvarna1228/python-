def is_sorted(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return False
    return True
a=[1,31,5,7,8]
print(is_sorted(a))