def missing(a):
    n = len(a) + 1 
    total_sum=n*(n+1)//2
    arr_sum = sum(a)
    return total_sum - arr_sum
a = [1, 2, 4, 5, 6]
missing_number = missing(a)
print(f"The missing number is: {missing_number}")