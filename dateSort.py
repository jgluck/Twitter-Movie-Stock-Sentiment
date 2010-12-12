from tweetReader import*
from dateConverter import *
import simplejson

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

def main():
    x = dayCorpusCount("harrypotter")
    for key in x.keys():
        print key + "---" + str(x[key])
if __name__=="__main__":
    main()

