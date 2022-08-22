'''Given a binary array nums, return the maximum number of consecutive 1's in the array.'''


def findMaxConsecutiveOnes(nums):
    l, output = 0, 0
    for r, n in enumerate(nums):
        if n == 0:
            l = r + 1
        output = max(output, r - l + 1)
    return output



print(findMaxConsecutiveOnes([1,1,1,0,1,1,0,1,1,1,1]))