class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        num = x
        while x > 0:
            rem = x % 10
            sum += rem
            x /= 10
        
        if num % sum == 0:
            return sum
        else:
            return -1
    