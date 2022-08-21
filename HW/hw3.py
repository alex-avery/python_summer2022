# Python Course - Summer 2022
# Homework 3
# Alex Avery

# Assignment instructions:
    # For the purposes of this exercise, we define three types of Twitter users.
        # Layman: Users with less than 100 followers
        # Expert: Users with 100-1000 followers
        # Celebrity: Users with more than 1000 followers
    # Using the Twitter API, and starting with the @WUSTLPoliSci twitter user, answer the following:
        # One degree of separation:
            # Among the followers of @WUSTLPoliSci who is the most active?
            # Among the followers of @WUSTLPoliSci who is the most popular, i.e. has the greatest number of followers?
            # Among the friends of @WUSTLPoliSci, i.e. the users she is following, who are the most active layman, expert and celebrity?
            # Among the friends of @WUSTLPoliSci who is the most popular?
        # Two degrees of separation: For the following two questions, limit your search of followers and friends to laymen and experts.
            # Among the followers of @WUSTLPoliSci and their followers, who is the most active?
            # Among the friends of @WUSTLPoliSci and their friends, who is the most active?

# import necessary modules
import os
import importlib 
import tweepy


# set directory to python course — homework folder
os.chdir('/Users/alexcisco/Library/Mobile Documents/com~apple~CloudDocs/Documents/WUSTL/Courses/Python Course/python_summer2022/HW')

# set up twitter api using authorization credintals called from file twitter_client.py
twitter = importlib.import_module('twitter_client')
api = twitter.client

# Create user objects
wustl = api.get_user(screen_name = '@WUSTLPoliSci')

# get number of followers
wustl.followers_count
followers = api.get_follower_ids(user_id = wustl.id)
len(followers)

# get number of friends 
wustl.friends_count
friends = api.get_friend_ids(user_id = wustl.id)
len(friends)

# -----------------------------------------------------------------------------   
# MOST ACTIVE FOLLOWER 


# get number of tweets for every follower of WUSTLPoliSci
counter = 0
max_tweets = 0

for follower in followers:
    counter +=1
    print(f"Working on follower {counter}.")
    try:
        if follower == followers[0]:
            max_tweets = api.get_user(user_id = follower)
        follower = api.get_user(user_id = follower)
        if follower.statuses_count > max_tweets.statuses_count:
            max_tweets = follower
    except tweepy.TweepyException:
        print("Error with user.")

# print the results for most active follower 
print(f"The most active follower(s) is/are {max_tweets.screen_name}.")

# -----------------------------------------------------------------------------

# MOST POPULAR FOLLOWER

# get number of followers for all folowers of WUSTL Poli Sci
counter = 0 
max_followers = 0 

for follower in followers:
    counter += 1
    print(f"Working on follower {counter}.")
    try:
        if follower == followers[0]:
            max_followers = api.get_user(user_id = follower)
        follower = api.get_user(user_id = follower)
        if follower.followers_count > max_followers.followers_count:
            max_followers = follower
    except tweepy.TweepyException:
        print("Error with user.")
    

# print the results for most popular follower 
print(f"The most popular follower(s) is/are {max_followers.screen_name}.")
                    
# -----------------------------------------------------------------------------

# MOST ACTIVE LAYMAN, EXPERT, AND CELEBRITY FRIENDS

#create empty lists for different types of twitter users 
counter = 0

layman = []
expert = []
celebrity = []

# sort users into lists
for friend in friends: 
    counter += 1
    print(f"Working on friend {counter}.")
    try:
        if friend == friends [0]:
            max_friend = api.get_user(user_id = friend)
        friend = api.get_user(user_id = friend)
        if friend.friends_count < 100:
            layman.append(friend)
        elif friend.friends_count >= 100 and friend.friends_count <= 1000:
            expert.append(friend)
        else:
            celebrity.append(friend)
    except tweepy.TweepyException:
        print("Error with user.")

# get number of tweets for every layman
counter = 0 
layman_tweets = 0

for l in layman:
    if l == layman[0]:
        layman_tweets = l
    counter += 1
    print(f"Working on layman {counter}.")
    if l.statuses_count > layman_tweets.statuses_count:
        layman_tweets = l

# print the results for most active layman 
print(f"The most active layman is/are {layman_tweets.screen_name}.")

# get number of tweets for every expert
counter = 0 
expert_tweets = 0

for e in expert:
    if e == expert[0]:
        expert_tweets = l
    counter += 1
    print(f"Working on expert {counter}.")
    if e.statuses_count > expert_tweets.statuses_count:
        expert_tweets = e

# print the results for most active layman 
print(f"The most active expert is/are {expert_tweets.screen_name}.")

# get number of tweets for every celebrity
counter = 0 
celebrity_tweets = 0

for c in celebrity:
    if c == celebrity[0]:
        celebrity_tweets = c
    counter += 1
    print(f"Working on celebrity {counter}.")
    if c.statuses_count > celebrity_tweets.statuses_count:
        celebrity_tweets = c

# print the results for most active layman 
print(f"The most active celebrity is/are {celebrity_tweets.screen_name}.")

# -----------------------------------------------------------------------------

# MOST POPULAR FRIEND

# get number of followers for all friends of WUSTL Poli Sci
counter = 0
max_friend = 0 

for friend in friends:
    counter += 1
    print(f"Working on friend {counter}.")
    try:
        if friend == friends[0]:
            max_friend = api.get_user(user_id = friend)
        friend = api.get_user(user_id = friend)
        if friend.followers_count > max_friend.followers_count:
            max_friend = friend 
    except tweepy.TweepyException:
        print("Error with user.")

# print the results for most popular friend 
print(f"The most popular friend(s) is/are {max_friend.screen_name}.")




