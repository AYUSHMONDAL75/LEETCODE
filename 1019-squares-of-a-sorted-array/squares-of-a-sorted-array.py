import math
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums)):
            square = nums[i]**2
            result.append(square)
            result.sort()
        return result