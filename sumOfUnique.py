def sumOfUnique(nums):
    nums2 = []
    for i in nums:
         if nums.count(i) == 1:
             nums2.append(i)
    return sum(nums2)



print(sumOfUnique([1,2,3,4,5,5,6,7,8,8,9,9]))