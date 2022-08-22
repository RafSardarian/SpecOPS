'''Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2'''


def missingNumber(nums):
    s = list(range(0, len(nums) - 1))
    y = list(set(s) - set(nums))
    return y[0]

print(missingNumber([4,1,3,0]))
print(missingNumber([0,2,3]))