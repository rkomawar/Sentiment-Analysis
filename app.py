from flask import Flask, redirect, render_template, request, url_for
import helpers, nltk, os, sys
from analyzer import Analyzer
from twython import Twython

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():

    positives = os.path.join(sys.path[0], 'positive-words.txt')
    negatives = os.path.join(sys.path[0], 'negative-words.txt')
    score = 0
    pnumb = 0
    nnumb = 0
    nenumb = 0
    count = 0


    analyzer = Analyzer(positives, negatives)

    # validate screen_name
    screen_name = request.args.get('screen_name', '')
    if not screen_name:
        return redirect(url_for('index'))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    
    for section in tweets:
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(section)
        for word in tokens:
            diff = analyzer.analyze(word)
            score = score + diff
        if score > 0.0:
            pnumb = pnumb + 1
            count = count + 1
        elif score < 0.0:
            nnumb = nnumb + 1
            count = count + 1
        else:
            nenumb = nenumb + 1
            count = count + 1



    positive, negative, neutral = ((pnumb/count) * 100), ((nnumb/count) * 100), ((nenumb/count) * 100)

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template('search.html', chart=chart, screen_name=screen_name)
