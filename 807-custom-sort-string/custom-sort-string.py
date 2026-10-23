
class Solution(object):
    def customSortString(self, order, s):
        ans = ""

        for i in range(len(order)):
            ans += order[i] * s.count(order[i])

        for i in range(len(s)):
            if s[i] not in order:
                ans += s[i]

        return ans
