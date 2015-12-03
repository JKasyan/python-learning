__author__ = 'evgen'

"""
1
"""
class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sum(self, i, j):
        sum = 0
        while i <= j:
            sum += self.nums[i]
            i += 1
        return sum

"""
2
"""

def twoSum(nums, target):
        length = len(nums)
        i = 0
        while not i == length - 1 :
            k = i + 1
            while not k == length:
                if nums[i] + nums[k] == target:
                    return [i+1, k+1]
                k += 1
            i += 1