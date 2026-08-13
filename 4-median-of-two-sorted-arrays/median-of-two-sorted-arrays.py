class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        marge = sorted(nums1 + nums2)
        n = len(marge)
        if(n % 2 == 1):
            return float (marge[n // 2])
        else :
            return float (marge[n // 2 - 1] + marge[n // 2]) / 2