class Solution(object):
    def removeStars(self, s):
        arr = []
        for i in range(len(s)):
            if s[i] == '*':
                arr.pop()
            else:
                arr.append(s[i])
                
        return "".join(arr)