class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        num = int("".join(map(str, num)))
        sum = num + k
        result = list(map(int, str(sum)))

        return result