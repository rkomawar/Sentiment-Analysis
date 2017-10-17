import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        self.positive = set()
        self.negative = set()
        p = open(positives, 'r') // file that contained positive words
        n = open(negatives, 'r') // file that contained negative words
        for line in p:
            self.positive.add(line.strip('\n'))
        for line in n:
            self.negative.add(line.strip('\n'))


        # TODO

    def analyze(self, text):
        count = 0;
        if text in self.positive:
            count = count + 1
        if text in self.negative:
            count = count - 1
        return count
