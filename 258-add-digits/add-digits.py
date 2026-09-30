class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        while num >= 10:
            sum = 0
            while num > 0:
                rem = num % 10
                sum = sum + rem
                num = num // 10
            num = sum
        return num