class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        strset = set()
        maxlen = 0
        l = 0
        for r in range(len(s)):
            while s[r] in strset:
                strset.remove(s[l])
                l += 1
            maxlen = max(maxlen, r-l+1)
            strset.add(s[r])
        
        return maxlen
        
        