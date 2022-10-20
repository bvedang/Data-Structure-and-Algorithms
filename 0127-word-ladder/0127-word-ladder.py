class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        wordList.append(beginWord)
        res = 1
        for word in wordList:
            for j in range(len(word)):
                patter = word[:j] + "*" + word[j+1:]
                adj[patter].append(word)
        visited = set()
        visited.add(beginWord)
        q = deque([beginWord])
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                visited.add(word)
                for j in range(len(word)):
                    patter = word[:j] + "*" + word[j+1:]
                    for neigh in adj[patter]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
            res += 1
        
        return 0