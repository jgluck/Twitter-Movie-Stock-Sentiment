from tweetReader import*
from dateConverter import *
import simplejson
import sys

def dayCorpusCount(tweetfilename):
    dates = {}
    decoder = simplejson.JSONDecoder()
    fp = open(tweetfilename,"r")
    while True:
        tweet = readTweet(fp,decoder)
        if tweet != None:
            date = tweet.getDate().split()
            #month = convertMonth(date[1])
            month = date[1]
            day = date[2]
            year = date[5]
            date = month + "\\" + day + "\\" + year
            if date in dates.keys():
                dates[date] +=1
            else:
                dates[date] = 1
        else:
            fp.close()
            return dates



def daySubjectivityCount(tweetfilename):
    dates={}
    decoder = simplejson.JSONDecoder()
    fp = open(tweetfilename,"r")
    while True:
        tweet = loadTweet(fp)
        if tweet != None:
            date = tweet.getDate().split()
            #month = convertMonth(date[1])
            month = date[1]
            day = date[2]
            year = date[5]
            date = month + "\\" + day + "\\" + year
            
            subj = tweet.getScore()
            positive = tweet.getPositive()
            negative = tweet.getNegative()
            
            if date in dates.keys():
                dates[date][0] += subj
                dates[date][1] += positive
                dates[date][2] += negative
            else:
               dates[date] = [subj,positive,negative,0]
        else:
            fp.close()
            return dates
                

def dayBasicCount(tweetfilename):
    dates={}
    decoder = simplejson.JSONDecoder()
    fp = open(tweetfilename,"r")
    while True:
        tweet = loadTweet(fp)
        if tweet != None:
            date = tweet.getDate().split()
            #month = convertMonth(date[1])
            month = date[1]
            day = date[2]
            year = date[5]
            date = month + "\\" + day + "\\" + year
            
            subj = tweet.getScore()
            positive = tweet.getPositive()
            negative = tweet.getNegative()
            
            if date in dates.keys():
                dates[date][0] += subj
                if positive >0:
                    dates[date][1] += 1 #positive
                if negative<0:
                    dates[date][2] += 1 #negative
            else:
                if positive>0 and negative<0:
                    dates[date] = [subj,1,1,0]
                elif positive >0:
                    dates[date] = [subj,1,0,0]
                elif negative<0:
                    dates[date] = [subj,0,1,0]
                else:
                    dates[date] = [subj,0,0,0]
        else:
            fp.close()
            return dates

def calculateScore(datedic):
    for key in datedic.keys():
        if datedic[key][2] != 0:
            datedic[key][3] = datedic[key][1]/float(datedic[key][2])
        else:
            datedic[key][3] = datedic[key][1]
    return datedic

def main():
    #x = dayCorpusCount(sys.argv[1])
    #x = daySubjectivityCount(sys.argv[1])
    x = dayBasicCount(sys.argv[1])
    x = calculateScore(x)
    for key in x.keys():
        print key + " " + str(x[key])
if __name__=="__main__":
    main()

