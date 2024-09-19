def duplicate(a):
    if not a:
        return[]
    result=[a[0]]
    for i in range(1,len(a)):
        if a[i]!=a[i-1]:
            result.append(a[i])
    return result
a = [1, 1, 2, 2, 3, 3, 4, 5, 5]
print(duplicate(a))