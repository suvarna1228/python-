def maxSumSubarray(arr):
    resStart = 0
    resEnd = 0
  
    
    maxSum = arr[0]

    for i in range(len(arr)):
        
        
        currSum = 0
        for j in range(i, len(arr)):
            currSum += arr[j]
            
            if currSum > maxSum:
                maxSum = currSum
                resStart = i
                resEnd = j
  
    res = []
    for i in range(resStart, resEnd + 1):
        res.append(arr[i])
    return res


arr = [2, 3, -8, 7, -1, 2, 3]
res = maxSumSubarray(arr)
  
for num in res:
    print(num, end=" ")
print()