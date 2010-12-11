import sys
import simplejson

def getTerms():
    terms = open("terms","r")
    dct = {}
    for line in terms:
        line = line.split("=")
        topic = line[0]
        termList = line[1].split(",")
        dct[topic] = termList
    rdct = {}
    for key in dct.keys():
        for term in dct[key]:
            rdct[term] = key
    return dct,rdct

def bigSort(fp,rdct,dct):
    for key in dct.keys():
        print "creating %s\n" %(key)
        vars()[key] = open(key,"a")
        
    decoder = simplejson.JSONDecoder()
    i = 0
    for line in fp:
        try:
            decoded = decoder.decode(line)
            if "text" not in decoded.keys():
                decoded["text"]=""
        except:
            decoded = {"text":""}
        for topic in dct.keys():
            for term in dct[topic]:
                if term in decoded["text"].lower():
                    eval(rdct[term]).write(line)



def main():
    termDict, rDct = getTerms()
    filename = sys.argv[1]
    fp = open(filename,"r")
    bigSort(fp,rDct,termDict)

main()
