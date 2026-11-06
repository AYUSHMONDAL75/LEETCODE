import math
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1 = max(nums)
        num2 = min(nums)
        while num2 != 0:
            rem = num1 % num2
            num1 = num2
            num2 = rem

        return num1