class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        count = 0
        num = 0
        for i in range(len(nums)):
            while nums[i] > 0:
                rem = nums[i] % 10
                nums[i] /= 10
                if rem == digit:
                    count += 1
        
        return count