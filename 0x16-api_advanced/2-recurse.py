#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries the Reddit API recursively and returns
    the titles of the first 10 hot posts"""

    if subreddit is None:
        print(None)
    if after:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Firefox/120.0'}

    res = requests.get(url=url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get("data", {})

        children = data.get("children", [])
        after = data.get("after", "")
        if children:
            for key in children:
                data = key.get("data", {})
                title = data.get("title", {})
                hot_list.append(title)
        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
