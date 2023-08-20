class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(sub):
            return(ord(sub) >= ord('a') and ord(sub) <= ord('z')) or (ord(sub) >= ord('0') and ord(sub) <= ord('9'))
        l,r = 0,len(s)-1
        while l < r:
            while l<r and not helper(s[l].lower()):
                l +=1
            while l < r and not helper(s[r].lower()):
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
            
        return True