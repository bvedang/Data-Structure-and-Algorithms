class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chardict = {}
        for char in chars:
            chardict[char] = 1 + chardict.get(char,0)
        res = 0
        for word in words:
            testdict = chardict.copy()
            count = 0
            for char in word:
                if char in testdict and testdict[char] > 0:
                    testdict[char] -= 1
                    count += 1
                    continue
                else:
                    break
            if len(word) == count:
                res += len(word)
        return res

                
                    