def find_unique_number(nums):
    unique_number = 0
    for num in nums:
        unique_number ^= num
    return unique_number


numbers = [2, 3, 5, 4, 5, 3, 2]
print(find_unique_number(numbers))  
