class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(i,j):
            while i<j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        i,j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return checkPalindrome(i+1,j) or checkPalindrome(i,j-1)
            i+=1
            j-=1
        return True