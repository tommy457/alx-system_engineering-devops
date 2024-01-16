#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def count_words(subreddit, word_list, after='', words_found={}):
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
                title = data.get("title", "").lower()

                for word in word_list:
                    word = word.lower()
                    if word in title:
                        current_count = words_found.get(word, 0)
                        words_found[word] = current_count + title.count(word)

        if after:
            return count_words(subreddit, word_list, after, words_found)
        else:
            words_found = sorted(
                    words_found.items(),
                    key=lambda x: (-x[1], x[0])
                    )
            for word, words_count in words_found:
                print("{}: {}".format(word, words_count))
            return
