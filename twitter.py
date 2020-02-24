"""
TWITTER API MODULE
"""
import json
import ssl
import urllib.error
import urllib.request

import twurl

FL_NAME = "file.json"
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def start(acct):
    """
    Main body
    """
    if len(acct) < 1:
        return
    try:
        url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()

        jsn = json.loads(data)
        with open(FL_NAME, encoding="utf-8", mode="w") as f_l:
            json.dump(jsn, f_l, indent=4, ensure_ascii=False)
        headers = dict(connection.getheaders())
        print('\nRemaining', headers['x-rate-limit-remaining'], '\n')
    except Exception:
        with open(FL_NAME, encoding="utf-8", mode="w") as f_l:
            json.dump([], f_l, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    start("max")
