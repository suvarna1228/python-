def binary_search(a, X):
    left, right = 0, len(a) - 1

    while left <= right:
        mid = left + (right - left) // 2  

       
        if a[mid] == X:
            return mid  
        
        elif a[mid] < X:
            left = mid + 1

       
        else:
            right = mid - 1

    return -1 


sorted_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X = 5
result = binary_search(sorted_a, X)

if result != -1:
    print(f"Element {X} found at index {result}.")
else:
    print(f"Element {X} not found in the a.")
