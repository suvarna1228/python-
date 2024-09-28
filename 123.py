def find_single_number(nums):
    unique_number = 0
    for num in nums:
        unique_number ^= num 
    return unique_number
numbers = [4, 1, 2, 1, 2]
print(find_single_number(numbers)) 
