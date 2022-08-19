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

#create empty lists for different types of twitter users 
laymen = []
expert = []
celebrity = 




