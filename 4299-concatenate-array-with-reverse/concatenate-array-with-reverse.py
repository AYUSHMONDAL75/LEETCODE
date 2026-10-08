class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1 = nums[::-1]
        total = nums + nums1
        return total