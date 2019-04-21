import os
from time import sleep
from sightengine.client import SightengineClient

import praw
import pdb
import re


API_USER = os.environ['SE_API_USER']
API_SECRET = os.environ['SE_API_SECRET']
client = SightengineClient(API_USER, API_SECRET)

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDDIT_USERNAME = os.environ['REDDIT_USERNAME']
REDDIT_PASS = os.environ['REDDIT_PASS']


def spot_celebs(image_url):
    output = client.check('celebrities').set_url(image_url)

    i = 1
    if output['faces']:
        reddit_comment = ""
        for face in output['faces']:
            if 'celebrity' in face:
                reddit_comment += 'Celebrity #' + str(i) + ': '

                if face['celebrity']:
                    if face['celebrity'][0]['prob'] > 0.85:
                        reddit_comment += face['celebrity'][0]['name'] + '\n'
                        i += 1
                    else:
                        reddit_comment += "unidentified"
                else:
                    reddit_comment += "unidentified"

                reddit_comment += '\n'
            else:
                reddit_comment = "None of the faces belong to a celebrity."

    else:
        reddit_comment = "No faces found in picture."

    reddit_comment += "\nBeep bop, I'm a bot."
    return reddit_comment


# Create the Reddit instance and log in
reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, password=REDDIT_PASS, user_agent='Recognises the faces of celebrities in the post.', username=REDDIT_USERNAME)

while True:
    subreddit = reddit.subreddit('all')
    for comment in subreddit.stream.comments():
        if '!SpotCelebsBot' in comment.body:
            comment.reply(spot_celebs(comment.link_url))
    sleep(2)


