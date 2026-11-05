import math
class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(len(nums)):
            x += nums[i]
        sum = 0

        for i in range(len(nums)):
            while nums[i] > 0:
                digit = nums[i] % 10
                sum += digit
                nums[i] = nums[i] // 10

        return abs(sum - x)