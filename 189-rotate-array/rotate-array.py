class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        arr1 = nums[-k:]
        arr2 = nums[:-k]
        nums[:] = arr1 + arr2