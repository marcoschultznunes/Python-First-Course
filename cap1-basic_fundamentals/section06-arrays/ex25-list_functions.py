nums = [1, 22, 14, 99, 53, 2, 26, 48]

# Splice 
print(nums[2:6]) # Get array from index 2 to 5
print(nums[:3]) # From 0 to 2
print(nums[5:]) # From 5 to end of array

# Inserting
nums[7:7] = [72, 80, 88, 96] # Inserts items at index 7, shifting the next indexes forward
print(nums)

# Replacing
nums[3: 7] = [11, 22] # Replaces, removing the extra items
print(nums)

# Sort
nums.sort()
print(nums)

nums.reverse()
print(nums)

# Copy
n2 = nums.copy()
print(n2)

n2[:9] = []
print(n2)
print(nums) # Deep copies instead of pointering
print()

# Count => Counts the number of elements with the specified value
print(nums.count(22))
print()

# Sum, Min, Max
print(sum(nums))
print(min(nums))
print(max(nums))