class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tdict, window = {},{}
        for char in t:
            tdict[char] = 1 + tdict.get(char,0)
        have,need = 0, len(tdict)
        res = [-1,-1]
        reslen = float("inf")
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char,0)
            if char in tdict and window[char] == tdict[char]:
                have += 1
            
            while have == need:
                if reslen > r-l+1:
                    reslen = r-l+1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in tdict and window[s[l]] < tdict[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        if reslen == float("inf"):
            return ""
        else:
            return s[l:r+1]
                