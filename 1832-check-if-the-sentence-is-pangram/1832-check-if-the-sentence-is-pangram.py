class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char = set()
        for chars in sentence:
            if ord('a') <= ord(chars) <= ord('z'):
                char.add(chars)
        
        if len(char) == 26:
            return True
        return False