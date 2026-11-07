class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digitSum = 0
        squareSum = 0
        while n > 0:
            rem = n % 10
            digitSum += rem
            squareSum += rem * rem
            n //= 10
        if squareSum - digitSum >= 50:
            return True
        else:
            return False