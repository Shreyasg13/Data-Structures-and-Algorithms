class Twitter:

    def __init__(self):
        
        self.post=0
        self.tweets=defaultdict(list)
        self.followMap=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweets[userId].append([self.post,tweetId])
        self.post -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:          
        res = []
        minHeap = [] 
        
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                post, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [post, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            post, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                post, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [post, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
            
        
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)