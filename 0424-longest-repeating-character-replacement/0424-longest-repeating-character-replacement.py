class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        l = 0
        length = 0
        maxf = 0
        for r in range(len(s)):
            charDict[s[r]] = 1+charDict.get(s[r],0)
            maxf = max(charDict[s[r]],maxf)
            if (r-l+1)-maxf > k:
                charDict[s[l]] -= 1
                l += 1
            length = max(length, r-l+1)
        return length