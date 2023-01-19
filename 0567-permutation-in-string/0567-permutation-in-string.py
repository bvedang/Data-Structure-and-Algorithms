class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = {}
        for char in s1:
            s1dict[char] = 1 + s1dict.get(char,0)
        
        window = len(s1)
        for i in range(len(s2)-window+1):
            s2dict = {}
            for j in range(i,i+window):
                s2dict[s2[j]] = 1 + s2dict.get(s2[j],0)
            if s1dict == s2dict:
                return True
        return False
                