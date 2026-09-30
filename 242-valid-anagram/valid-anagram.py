class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str1 = s.lower()
        str2 = t.lower()
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False