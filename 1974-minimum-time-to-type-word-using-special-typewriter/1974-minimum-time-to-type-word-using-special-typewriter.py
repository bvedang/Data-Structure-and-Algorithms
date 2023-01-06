class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        prev = 'a'
        for char in word:
            dist = (ord(char) - ord(prev)) % 26
            dist = min(dist, 26 - dist)
            prev = char
            time += dist + 1
        return time