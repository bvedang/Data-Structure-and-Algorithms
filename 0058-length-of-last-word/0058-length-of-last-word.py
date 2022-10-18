class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strlist = s.split(" ")
        print(strlist)
        for i in range(len(strlist)-1,-1,-1):
            if strlist[i] == "":
                continue
            return len(strlist[i])