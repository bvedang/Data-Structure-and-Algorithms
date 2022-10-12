class Twitter:

    def __init__(self):
        self.userfollow = defaultdict(set)
        self.userposts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -=1
        self.userposts[userId].append((self.time, tweetId))
        self.userfollow[userId].add(userId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res =[]
        minheap = []
        for user in self.userfollow[userId]:
            if len(self.userposts[user]) <= 10:
                for i in self.userposts[user]:
                    minheap.append(i)
            if len(self.userposts[user]) >10:
                 for i in range(10,-1,-1):
                    minheap.append(self.userposts[user][i])
                    
        heapq.heapify(minheap)
        while minheap and len(res) <10:
            time, tweetId = heapq.heappop(minheap)
            res.append(tweetId)
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.userfollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userfollow[followerId]:
            self.userfollow[followerId].remove(followeeId)
        else:
            return
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)