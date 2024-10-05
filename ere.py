def find_majority_element(nums):
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num
    return None

nums = [2, 2, 1, 1, 1, 2, 2]
result = find_majority_element(nums)
print("Majority Element:", result)
