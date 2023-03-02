from itertools import product, combinations, combinations_with_replacement
import math
import random
import sys
import collections
from pathlib import Path
import bisect
import math
from typing import List

import numpy as np

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


import copy

class Twitter:

    def __init__(self):
        self.follow_list = {}
        self.tweets = {}
        self.i_tweet = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets.keys():
            self.tweets[userId].append((self.i_tweet, tweetId))
        else:
            self.tweets[userId] = [(self.i_tweet, tweetId)]
        self.i_tweet += 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.tweets.keys():
            _tweets = []  # usedId does not tweet yet.
        else:
            _tweets = copy.deepcopy(self.tweets[userId])
    
        if userId in self.follow_list.keys():
            for followeeId in self.follow_list[userId]:
                if followeeId in self.tweets.keys():
                    _tweets += self.tweets[followeeId]
        else:
            ...  # does not follow anyone yet

        news = []
        for index_and_tweet in sorted(_tweets, key=lambda x: x[0], reverse=True):
            news.append(index_and_tweet[1])
        return news[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_list.keys():
            self.follow_list[followerId].add(followeeId)
        else:
            self.follow_list[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_list:
            self.follow_list[followerId] = self.follow_list[followerId].remove(followeeId)
            if self.follow_list[followerId] is None:
                self.follow_list[followerId] = {}


def q_355_top():
    if DEBUG_OUT:
        t = Twitter()
        t.postTweet(*[1, 5])
        print(t.getNewsFeed(*[1]))
        t.follow(*[1, 2])
        t.postTweet(*[2, 6])
        print(t.getNewsFeed(*[1]))
        t.unfollow(*[1, 2])
        print(t.getNewsFeed(*[1]))

        t = Twitter()
        t.postTweet(*[1,5])
        t.postTweet(*[1,3])
        t.postTweet(*[1,101],)
        t.postTweet(*[1,13],)
        t.postTweet(*[1,10],)
        t.postTweet(*[1,2],)
        t.postTweet(*[1,94],)
        t.postTweet(*[1,505],)
        t.postTweet(*[1,333],)
        t.postTweet(*[1,22],)
        t.postTweet(*[1,11])
        print(t.getNewsFeed(*[1]))

    
if __name__ == "__main__":
    q_355_top()
