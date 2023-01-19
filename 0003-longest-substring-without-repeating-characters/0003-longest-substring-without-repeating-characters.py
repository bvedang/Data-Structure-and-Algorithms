class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        charset = set()
        l = 0
        longestStrlen = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            longestStrlen = max(longestStrlen, r-l+1)
        
        return longestStrlen