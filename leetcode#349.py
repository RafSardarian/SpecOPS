'''349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
#  Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
#  Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
'''


def intersection(nums1,nums2):
    return list(set(nums2) - (set(nums2) - set(nums1)))

print(intersection([1,2,3,4,5,6],[1,1,3,6]))
print(intersection([1,1,2,2],[1,2,3,15]))