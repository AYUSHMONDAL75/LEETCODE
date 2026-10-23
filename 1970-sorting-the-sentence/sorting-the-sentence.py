class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        res = ["" for _ in range(len(words))]

        for word in words:
            pos = int(word[-1]) - 1
            res[pos] = word[:-1]
            
        return " ".join(res)