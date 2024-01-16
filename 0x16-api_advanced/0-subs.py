#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API,
    returns the number of subscribers"""
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Firefox/120.0'}

    res = requests.get(url=url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get("data", {})
        return data.get("subscribers", 0)
    return 0
