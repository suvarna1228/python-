def longest_subarray_with_sum_k(arr, k):
    start = 0
    current_sum = 0
    max_length = 0

    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > k:
            current_sum -= arr[start]
            start += 1
    
        if current_sum == k:
            max_length = max(max_length, end - start + 1)
    
    return max_length
arr = [1, 2, 3, 7, 5]
k = 12
print(longest_subarray_with_sum_k(arr, k))  
