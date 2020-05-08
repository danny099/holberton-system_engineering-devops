#!/usr/bin/python3
"""
reddit api
"""
import requests


def recurse(subreddit, hot_list=[], after=""):

    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    headers = {'User-Agent': 'danny'}
    r = requests.get(url, headers=headers).json()
    try:
        for i in r.get('data')['children']:
            hot_list.append(i['data']['title'])
        if r['data']['after'] is not None:
            recurse(subreddit, hot_list, r['data']['after'])
        return hot_list
    except Exception:
        return None
