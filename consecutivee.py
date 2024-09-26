def consecutive(nums):
    maxe=0
    counte=0
    for num in nums:
        if num==1:
            counte=counte+1
            maxe=max(maxe,counte)
        else:
            counte=0
    return maxe
nums = [1, 1, 0, 1, 1, 1]
print(consecutive(nums)) 