'''1748. Sum of Unique Elements
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.
#  Example 1:
Input: nums = [1,2,3,2]
Output: 4
#  Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
#  Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
'''

def sumOfUnique(nums):
    nums2 = []
    for i in nums:
        if nums.count(i) == 1:
            nums2.append(i)
    return sum(nums2)

print(sumOfUnique([1,1,2,3,4,3,5,5,6]))
print(sumOfUnique([2,2,2,2]))
print(sumOfUnique([1,2,3,4,5]))