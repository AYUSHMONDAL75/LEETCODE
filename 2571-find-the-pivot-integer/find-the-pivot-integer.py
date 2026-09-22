import math

class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_sum = (n * (n + 1)) // 2
        pivot = math.sqrt(total_sum)
        if pivot == int(pivot):
            return int(pivot)
        
        return -1