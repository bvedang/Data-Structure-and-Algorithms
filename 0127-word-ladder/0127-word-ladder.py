class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        wordList.append(beginWord)
        graph = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                patter = word[:j] + "*" + word[j+1:]                            ## getting all patter hit -> h*t, *ot, ho* and all its adjacent words
                graph[patter].append(word)
        
        
        visited = set()
        visited.add(beginWord)
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                for j in range(len(node)):
                    patter = node[:j] + "*" + node[j+1:]
                    for neighbor in graph[patter]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            res += 1
            
        return 0