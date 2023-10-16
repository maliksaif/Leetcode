digits = [1,2,3]
combinedNumber = ""

# N 
for digit in digits:
    combinedNumber += str(digit)

digits = []
combinedNumber = str(int(combinedNumber) + 1 )

# N 
for digit in str(combinedNumber):
    digits.append(int(digit))

# With comprehension


print(digits)