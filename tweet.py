#!/usr/bin/env python3
import sys
from twython import Twython
import nltk
import os
from analyzer import Analyzer
from termcolor import colored


API_KEY = '****'
API_SECRET = '****' // removed for upload
twitter = Twython(API_KEY, API_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
t = Twython(API_KEY, access_token=ACCESS_TOKEN)


def main():
    positives = os.path.join(sys.path[0], 'positive-words.txt')
    negatives = os.path.join(sys.path[0], 'negative-words.txt')
    score = 0

    analyzer = Analyzer(positives, negatives)
    name = sys.argv[1]
    if len(sys.argv) != 2:
        print ('Not right number of command-line arguments')
        sys.exit(0)
    results = t.get_user_timeline(count=50, screen_name=name, exclude_replies=True)
    for tweets in results:
        more = tweets['text']
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(more)
        for word in tokens:
            diff = analyzer.analyze(word)
            score = score + diff
        if score > 0.0:
            print(colored(print(tweets['text'], end=''), 'green'))
        elif score < 0.0:
            print(colored(print(tweets['text'], end=''), 'red'))
        else:
            print(colored(print(tweets['text'], end=''), 'yellow'))
        print()


if __name__ == '__main__':
    main()



