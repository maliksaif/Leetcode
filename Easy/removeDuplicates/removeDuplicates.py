   
nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = []
tempNums = nums[:]

for num in tempNums:
    if num not in expectedNums:
        expectedNums.append(num)
    else:
        # originalList.append(num)
        nums.remove(num)