#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and returns
    the titles of the first 10 hot posts"""

    if subreddit is None:
        print(None)
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Firefox/120.0'}

    res = requests.get(url=url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get("data", {})

        children = data.get("children", {})
        if children:
            for key in children[:10]:
                data = key.get("data", {})
                title = data.get("title", {})
                print(title)
    else:
        print(None)
