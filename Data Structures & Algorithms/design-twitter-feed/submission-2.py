from heapq import heapify, heappush, heappop

class Twitter:

    def __init__(self):
        # What to store: Tweets(related to user), follows(follower, followee)
        # Need a way to store feed for a user, which only contains tweets from their followers

        # We can use a hashmap to store users(keys) and their tweets(values, List[tweets])
        # Only 10 newest tweets are required for each user
        # We can store only 10 tweets and remove oldest tweet when new one is added
        # We can use a min heap to remove oldest post
        self.tweets = {}

        # Followers can also be stored using a hashmap
        # Each user(key) can have a set of followers(value, Tuple(users))
        self.follows = {}

        # Need a global time to synchronize new tweets
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # When a user posts a tweet, we insert it into the self.tweets heap
        # O(log n) time to add new tweet
        if userId in self.tweets:
            # insert a tuple to make sure heap is arranged based on time
            if len(self.tweets[userId]) == 10:
                heappop(self.tweets[userId])
            heappush(self.tweets[userId], (self.time, tweetId))
        else:
            self.tweets[userId] = []
            heapify(self.tweets[userId])
            heappush(self.tweets[userId], (self.time, tweetId))
        print("Posted: ", self.tweets)
        # Time only needs to be updated when new tweets are posted
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followList = self.follows[userId] if userId in self.follows else set()
        followList.add(userId)
        followList = list(followList)
        print(f"Follow list {userId}: ", followList)
        feed = []
        for followee in followList:
            posts = self.tweets[followee] if followee in self.tweets else []
            feed.extend(posts)
        feed = sorted(feed, reverse=True)
        print("Sorted feed: ", feed)
        if len(feed) > 9:
            return [tweetId for time, tweetId in feed[:10]]
        return [tweetId for time, tweetId in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            # We use sets because each user can follow a followee only once
            # And all users are unique
            self.follows[followerId] = set()
            # Follower should follow themselves as well
            self.follows[followerId].add(followerId)
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        else:
            print("Follower doesn't follow anyone.")
