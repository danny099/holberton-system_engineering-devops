#!/usr/bin/python3
"""
reddit api
"""
import requests


def number_of_subscribers(subreddit):
    if type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'chrome:happy/0.1.0'}
    data = requests.get(url, headers=headers)
    if data.status_code != 200:
        return 0
    return data.json().get("data").get("subscribers")
