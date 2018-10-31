import getpass
import hashlib
import os
import time

from tasks import scrape_images, send_tweet, what_guido_says, bonus_catzz


def test_send_tweet():
    res = send_tweet('{} says hi! (Timestamp: {})'
                     .format(getpass.getuser(), int(time.time())))
    assert int(res['status']) == 200


def test_what_guido_says():
    assert what_guido_says("2018-10-22", "2018-10-28", "Python") == [
        ("@sukhiyadeep22 Please file a more detailed bug report at https://t.co/GjFaGfmq3M.", False)
    ]

    assert what_guido_says("2018-10-20", "2018-10-24", "Tech") == [
        ("RT @OracleDevs: #CodeOne18 Groundbreakers Panel: Tech Trends discussion https://t.co/EnwzB4TvRZ", True)
    ]


def test_scrape_images():
    scrape_images('https://gvanrossum.github.io/')

    files = [
        ("IMG_2192.jpg", "3acd8b703ba49e8c55665a671b8f7fc1"),
        ("license_thumb.jpg", "4a102f542d23a831362d0e0366a4dd3d")
    ]

    assert all([os.path.isfile(f) and md5(f) == hash for (f, hash) in files])


def test_bonus_catzz():
    bonus_catzz()


# https://stackoverflow.com/a/3431838/1107768
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
