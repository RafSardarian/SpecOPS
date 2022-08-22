'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
We must implement a solution with a linear runtime complexity and use only constant extra space.

#  Example 1:
Input: nums = [2,2,1]
Output: 1
#  Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
#  Example 3:
Input: nums = [1]
Output: 1
'''


def singleNumber(nums):
    x = 0
    for i in nums:
        x ^= i
    return x

print(singleNumber([4,1,1,2,2,3,3]))
print(singleNumber([1,2,2,3,4,3,4,1,0]))