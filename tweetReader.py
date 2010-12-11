#!/user/bin/env python

import simplejson

class tweet(object):
    
    def __init__(self,twit):
        self.text = twit["text"].encode("UTF-8")
        self.textList = self.text.split()
        self.PoS = []
        self.contributors = twit["contributors"]
        self.dic = twit
        self.date = twit["created_at"]
        self.positive = 0
        self.negative = 0
        self.total = 0
        self.nText = self.text
        self.nText = self.nText.replace("not ","not-")

    def changeScore(self,n):
        if n>=0:
            self.positive += n
        else:
            self.negative += n
        self.total += n
    def getScore(self):
        return self.total

    def getText(self):
        return self.text

    def getDate(self):
        return self.date
    
    def getnText(self):
        return self.nText

def readTweets(fname):
    lines = []
    fp = open(fname,"r")
    decoder = simplejson.JSONDecoder()
    for line in fp:
        lines.append(tweet(decoder.decode(line)))
    return lines


if __name__=="__main__":
    main()
