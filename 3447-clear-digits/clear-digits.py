class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans =  ""

        for c in s:
            if c.isdigit():
                ans = ans[:-1]
            else:
                ans += c

        return ans
