class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = int("".join(map(str, digits)))
        temp = result + 1
        digit_list = list(map(int, str(temp)))
        return digit_list