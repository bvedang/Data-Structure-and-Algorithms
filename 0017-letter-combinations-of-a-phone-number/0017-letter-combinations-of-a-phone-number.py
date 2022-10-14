class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res =[]
        digitstr = { "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits) == 1:
            for char in digitstr[digits[0]]:
                res.append(char)
            return res
        def backtrack(i,currstr):
            if len(currstr) == len(digits):
                res.append(currstr)
                return
            for char in digitstr[digits[i]]:
                backtrack(i+1, currstr+char)
        backtrack(0,"")
        return res