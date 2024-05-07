#!/usr/bin/python3

"""
Script queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit

    :If not a valid subreddit, return 0
    : Invalid subreddits may return a redirect to search results.
        Ensure that you are not following redirects.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return: Number of subscribers for a given subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
