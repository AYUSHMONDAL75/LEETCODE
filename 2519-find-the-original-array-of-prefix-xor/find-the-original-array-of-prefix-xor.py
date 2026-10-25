class Solution(object):
    def findArray(self, pref):
        return [pref[i] ^ pref[i - 1] if i > 0 else pref[0] for i in range(len(pref))]