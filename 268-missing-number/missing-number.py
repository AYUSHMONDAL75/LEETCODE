class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        ans = 0
        for i in range(0, len(nums) + 1):
            ans ^= i
        for i in range(len(nums)):
            xor ^= nums[i]

        return ans ^ xor