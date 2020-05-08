#!/usr/bin/python3
"""
reddit api
"""
import requests


def top_ten(subreddit):
    posts = ""
    if type(subreddit) is not str:
        posts = "None\n"
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'user-agent': 'chrome:happy/0.1.0'}
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            posts = "None\n"
        else:
            data_json = r.json().get("data").get("children")
            for i in range(10):
                post = data_json[i].get("data").get("title")
                posts += "{}\n".format(post)
    print(posts, end="")
