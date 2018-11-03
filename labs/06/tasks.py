import json
import os
import re
from urllib.parse import urlencode
from datetime import datetime

import requests

"""
TODO: paste tokens from e-mail into utils
TODO: $ pip install requests oauth2
"""
from utils import create_client

# Twitter API documentation: https://developer.twitter.com/en/docs.html
API_URL = 'https://api.twitter.com/1.1/'
CLIENT = create_client()


def send_tweet(status):
    """
    1 point.
    Send a tweet with the given `status`.
    Return the response from client.request call.

    Use the provided `CLIENT` variable. Don't forget to urlencode the
    URL parameters.

    Example:
        res = send_tweet('Hello!')
        assert int(res['status']) == 2OO
    """
    client = create_client()
    url = API_URL + 'statuses/update.json?' + urlencode({'status': status})
    res, data = client.request(
        url,
        method="POST", headers={
            "content-type": "application/json"
        })
    assert res['status'] == '200'
    return res


def what_guido_says(since, until, keyword, account='gvanrossum'):
    """
    2 points.
    Return a list of tweets originating from the Twitter account 'gvanrossum'
    that were posted between `since` and `until` and contain `keyword`.
    Each entry in the list should be a tuple (tweet_text, is_retweet).
    tweet_text should be the text of the tweet
    is_retweet is a boolean stating whether the tweet is a retweet or not

    Use the provided `CLIENT` variable. Don't forget to urlencode the
    URL parameters.

    Example:
        what_guido_says('2018-10-20', '2018-10-25', 'Python')
        # [('blabla', False), ('RT: blablabla', True)]
    """
    client = create_client()
    url = API_URL + 'statuses/user_timeline.json?' + urlencode({'screen_name': account})
    res, data = client.request(
        url,
        method="GET", headers={
            "content-type": "application/json"
        })
    assert res['status'] == '200'

    tweets = json.loads(data)

    ret = []

    for tweet in tweets:
        created_at = tweet.get('created_at')

        since_timestamp = datetime.strptime(since, '%Y-%m-%d').timestamp()
        until_timestamp = datetime.strptime(until, '%Y-%m-%d').timestamp()
        created_at_timestamp = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y').timestamp()

        text = text_for_search = tweet.get('text')
        is_retweet = None is not tweet.get('retweeted_status')

        for i in tweet.get('entities'):
            if i == 'urls':
                for j in tweet.get('entities')[i]:
                    text_for_search = text.replace(j['url'], j['expanded_url'])

        if (since_timestamp <= created_at_timestamp) and \
                (created_at_timestamp <= until_timestamp) and \
                (keyword.lower() in text_for_search.lower()):
            ret.append((text, is_retweet))

    return ret


def scrape_images(url):
    """
    3 points.
    Download the web page from the given `url` and find all images on the page.
    Then download each image and write it to the filesystem under its filename.

    Regex cheatsheet: https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285

    Example:
        Web page asd.cz: <html>....<img src="images/ahoj.jpg" />...</html>

        scrape_images('http://asd.cz')
        # creates file 'ahoj.jpg' with the image content ('images/' is ignored)

    Hint:
        Either download the web page and parse the images using regular expressions,
        or use the MechanicalSoup (https://mechanicalsoup.readthedocs.io/en/stable/tutorial.html)
        library to extract images from the page.
    """
    pass


def bonus_catzz():
    """
    1 point (bonus).
    Download the latest 10 tweets from the Twitter account CatMemes.
    Download all images contained in those tweets and combine them into
    one large image containing the latest cat memes. Write the collage image
    to the filesystem.

    Hint: use the pillow library to merge images together
    """
    pass
