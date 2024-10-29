def subarray(a,k,):
    n=len(a)
    cnt=0
    for i in range(n):
        for j in range(i, n): 
            subarray = sum(a[i:j+1])
            if subarray == k:
                cnt += 1
    return cnt
    
a=[3,1,5,4]
k=6
cnt=subarray(a,k)
print(cnt)