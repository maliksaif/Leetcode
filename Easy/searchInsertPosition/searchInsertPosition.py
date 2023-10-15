nums = [1,3]
target = 2

# Approach 
# Searching Algorithm with time complexity of O(log n ) - Binary Search 

# Binary Search has start, mid , end 
start = 0
end = len(nums) - 1
result = -1

# Initial checks
# if the values the greater than last value in array/list
if target > nums[end]:
    result = end + 1
    
# if the values the lesss than first value in array/list
if target < nums[start]:
    result = start 

# Searching for the value iteratively using binary search
while start<= end:
    mid = ( start + end ) // 2
    currentValue = nums[mid]
    # If value matches our target 
    if currentValue == target :
        result = mid 
        break
    if mid < end and target > currentValue and target < nums[mid + 1]:
        result = mid + 1
        break 
    if currentValue > target:
        end = mid - 1 
    else:
        start = mid + 1

print(result)
