class Solution(object):
    def twoSum(self, nums, target):
        arr = sorted((nums[i], i) for i in range(len(nums)))
        left = 0
        right = len(arr) - 1
        while left < right:
            sum = arr[left][0] + arr[right][0]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [arr[left][1], arr[right][1]]