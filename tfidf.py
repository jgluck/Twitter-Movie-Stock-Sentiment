#!/usr/bin/env python

import nltk
from extractSubjectivity import *
from tweetReader import *
from math import *
from operator import itemgetter

def freq(word,document):
    word = word.lower()
    document = document.lower()
    x= document.split(None).count(word)
    return x
def wordCount(document):
    return len(document.split(None))

def numDocsContaining(word,documentList):
    count = 0
    for document in documentList:
        if freq(word,document["text"]) > 0:
            count += 1
    return count

def tf(word,document):
    return (freq(word,document)/float(wordCount(document)))

def idf(word,documentList):
    return log(len(documentList)/numDocsContaining(word,documentList))

def tfidf(word,document,documentList):
    return (tf(word,document) * idf(word,documentList))

def simpleSubjectivity(subjfilename,tweetfilename,strength=False):
    sentiments = weibe(subjfilename,strength)
    tweets = readTweets(tweetfilename)
    for tweet in tweets:
        for word in sentiments[2]:
            tweet.changeScore(word.getPolarity()*freq(word.getText(),tweet.getText()))
    return tweets

def negatedSubjectivity(subjfilename,tweetfilename,strength=False):
    sentiments = weibe(subjfilename,strength)
    tweets = readTweets(tweetfilename)
    for tweet in tweets:
        for word in sentiments[2]:
            tweet.changeScore(word.getPolarity()*freq(word.getText(),tweet.getnText()))
    return tweets

def taggedSubjectivity(subjfilename, tweetfilename,strength=False):
    sentiments = weibe(subjfilename,strength)

def main():
    tweets = simpleSubjectivity("subjclues.tff","tangled2")
    for tweet in tweets:
        print tweet.getText(), tweet.getScore()

main()
