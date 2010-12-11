#!/usr/bin/env python

import nltk
import sys
from extractSubjectivity import *
from tweetReader import *
from math import *
from operator import itemgetter

def freq(word,document):
    word = word.lower()
    document = document.lower()
    x= document.split(None).count(word)
    return x

def freq_pos(word,document):
    word_pos = word.getPos()
    word = word.getText()
    count = 0
    for pair in document:
        if word == pair[0] and pair[1] == word_pos:
            count+=0
    return count

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


##not working right now
def taggedSubjectivity(subjfilename, tweetfilename,strength=False):
    
    def tagConverter(taglist):
        new = []
        for word in taglist:
            tag = word[1]
            if tag == 'NN':
                new.append((word[0].lower(),"noun"))
            elif tag == 'JJ':
                new.append((word[0].lower(),"adj"))
            elif tag == 'JJR':
                new.append((word[0].lower(),"adj"))
            elif tag == 'JJS':
                new.append((word[0].lower(),"adj"))
            elif tag == 'MD':
                new.append((word[0].lower(),"verb"))
            elif tag == 'NNP':
                new.append((word[0].lower(),"noun"))
            elif tag == 'RB':
                new.append((word[0].lower(),"adverb"))
            elif tag == 'VB':
                new.append((word[0].lower(),"verb"))
            elif tag == 'VBD':
                new.append((word[0].lower(),"verb"))
            elif tag == 'VBG':
                new.append((word[0].lower(),"verb"))
            elif tag == 'VBN':
                new.append((word[0].lower(),"verb"))
        return new
    
    sentiments = weibe(subjfilename,strength)
    tweets = readTweets(tweetfilename)
    for tweet in tweets:
        taggedTweet = tagConverter(nltk.pos_tag(nltk.word_tokenize(tweet.getText())))
        for word in sentiments[2]:
            tweet.changeScore(word.getPolarity()*freq_pos(word,taggedTweet))
    return tweets
    nltk.word_tokenize


def main():
    if len(sys.argv) != 3:
        print "propper call 'python tfidf <savedestination> <strength s or w>'"
        exit()
    if sys.argv[2] == "s":
        strength = True
    else:
        strength = False
    fp = open(sys.argv[1],"w")
    tweets = negatedSubjectivity("subjclues.tff-neg","tangled2",strength)
    #tweets = simpleSubjectivity("subjclues.tff","tangled2")
    #tweets = taggedSubjectivity("subjclues.tff","tangled2")
    for tweet in tweets:
        tweet.save(fp)
    fp.close()

main()
