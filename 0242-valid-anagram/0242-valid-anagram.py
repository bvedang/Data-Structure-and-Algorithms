class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        return self.uniqueChar(s) == self.uniqueChar(t)
    
    def uniqueChar(self,word:str)->dict:
        charDict = {}
        for char in word:
            if char in charDict:
                charDict[char] +=1
            else:
                charDict[char] = 1
        return charDict
#         first check if length of both string is equal or not
        