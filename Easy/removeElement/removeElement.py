    # This problem is pretty much same as the last one. 
    # I am going to follow the same approach. 

nums = [3,2,2,3]
val = 3
expectedNums = [] # Output List
tempNums = nums[:] # Making copy to remove the list [:] so list is copied by value not  reference

for num in tempNums:
    if num == val:
    # Remove number from original list
        nums.remove(num)
    else:
# Add number in new list
        expectedNums.append(num) 

