#!/usr/bin/python3
"""
reddit api
"""
import requests


def number_of_subscribers(subreddit):
    if type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'danny'}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return 0
    return r.json().get("data").get("subscribers")
