class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res =[]
        ptr1 = ptr2 = 0
        while ptr1 < len(word1) or ptr2 < len(word2):
            if ptr1<len(word1) and ptr2 < len(word2):
                res.append(word1[ptr1])
                res.append(word2[ptr2])
                ptr1 +=1
                ptr2 +=1
            elif ptr1<len(word1) and ptr2 == len(word2):
                res.append(word1[ptr1])
                ptr1 +=1
            elif ptr2 < len(word2) and ptr1 == len(word1):
                res.append(word2[ptr2])
                ptr2 +=1
        return "".join(res)