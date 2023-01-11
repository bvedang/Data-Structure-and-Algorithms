class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            wordKey = [0]*26
            for char in word:
                wordKey[ord(char) - ord('a')] += 1
            
            groups[tuple(wordKey)].append(word)
        
        return groups.values()
        