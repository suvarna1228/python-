def longest_subarray_with_sum_k(arr, K):
    sum_map = {}  
    curr_sum = 0  
    max_len = 0  

    for i in range(len(arr)):
        curr_sum += arr[i]  

        if curr_sum == K:
            max_len = i + 1

       
        if (curr_sum - K) in sum_map:
            max_len = max(max_len, i - sum_map[curr_sum - K])

       
        if curr_sum not in sum_map:
            sum_map[curr_sum] = i

    return max_len


arr = [1, -1, 5, -2, 3]
K = 3
print(longest_subarray_with_sum_k(arr, K)) 
