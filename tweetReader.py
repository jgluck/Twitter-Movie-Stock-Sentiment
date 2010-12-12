#!/user/bin/env python

import simplejson

class tweet(object):
    
    def __init__(self,twit=None):
        if twit!=None:
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
        else:
            self.text = None
            self.contributors = None
            self.dic = None
            self.date = None
            self.positive = None
            self.negative = None
            self.total = None

    def save(self,fp):
        encoder = simplejson.JSONEncoder()
        self.dic["positive"] = self.positive
        self.dic["negative"] =  self.negative
        self.dic["total"] = self.total
        line = encoder.encode(self.dic) + "\n"
        fp.write(line)



    def load(self,line):
        decoder = simplejson.JSONDecoder()
        self.dic = decoder.decode(line)
        self.text = self.dic["text"].encode("UTF-8")
        self.date = self.dic["created_at"]
        self.positive = self.dic["positive"]
        self.negative = self.dic["negative"]
        self.total = self.dic["total"]
        self.nText = self.text.replace("not ","not-")

    
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

def readTweet(fp,decoder):
    try:
        return tweet(decoder.decode(fp.readline()))
    except:
        return None


if __name__=="__main__":
    main()
