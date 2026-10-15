import math
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        num = int("".join(map(str, b)))
        return pow(a, num, 1337)
