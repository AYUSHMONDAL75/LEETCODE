class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        nums.sort()
        answer = 0
        for i in range(0, len(nums)):
            if i + 2 < len(nums):
                if nums[i] + nums[i + 1] > nums[i + 2]:
                    perimeter = nums[i] + nums[i + 1] + nums[i + 2]
                    if perimeter > answer:
                        answer = perimeter
        return answer