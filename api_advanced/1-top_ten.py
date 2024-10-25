#!/usr/bin/python3
"""Module that queries the Reddit API for the top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    try:
        response = requests.get(reddit_url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            if not data:
                print(None)
            else:
                for post in data:
                    print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)

