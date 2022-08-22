'''34. Find First and Last Position of Element in Sorted Array.
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
#  Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
#  Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
#  Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''


def searchRange(nums, target):
    left = binSearch(nums, target, True)
    right = binSearch(nums, target, False)
    return [left, right]


def binSearch(nums, target, leftBias):
    l, r = 0, len(nums) - 1
    i = -1
    while l <= r:
        m = (l + r) // 2
        if target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1
        else:
            i = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1
    return i


print(searchRange([1, 2, 3, 4, 5, 8, 8, 8, 8, 9], 8))
print(searchRange([1,1,1,2,2,2,3,3,4,5,6,7,8],2))