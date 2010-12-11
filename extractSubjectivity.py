class subjword(object):
    def __init__(self):
        self.strength = None
        self.polarity = None
        self.text = None
        self.pos = None
        self.tfidf = None
    
    def __str__(self):
        return self.text + " " + str(self.polarity)
    
    def __len__(self):
        return len(self.text)

    def __eq__(self,other):
        return self.text == other.getText()
    def __nq__(self,other):
        return not self.__eq__(other)

    # mutators
    def setTfidf(self,t):
        self.tfidf = t
    def setStrength(self,s):
        self.strength = s
    def setPolarity(self,p):
        self.polarity = p
    def setText(self,t):
        self.text = t
    def setPos(self,p):
        self.pos = p
    
    #getters
    def getTfidf(self):
        return self.tfidf
    def getStrength(self):
        return self.strength
    def getPolarity(self):
        return self.polarity
    def getText(self):
        return self.text
    def getPos(self):
        return self.pos



def weibe(filename,strong=False):
    fp = open(filename,"r")
    positive = []
    negative = []
    both = []
    for line in fp:
        if line[0] != "#":
            flag = False
            if strong:
                line = line.split()
                if line[0] == "type=strongsubj":
                    entry = subjword()
                    #print line
                    if line[0].split("=")[1] == "strongsubj":
                        entry.setStrength(1) #strong
                    else:
                        entry.setStrength(0) #weak
                    entry.setText(line[2].split("=")[1])
                    if len(both)>0 and entry == both[-1]:
                        flag=True
                    entry.setPos(line[3].split("=")[1])
                    if line[5].split("=")[1] == "negative":
                        entry.setPolarity(-1)
                    else:
                        entry.setPolarity(1)
                    if entry.getPolarity() == 1 and not flag:
                        positive.append(entry)
                        both.append(entry)
                    elif not flag:
                        negative.append(entry)
                        both.append(entry)
            else:
                entry = subjword()
                line = line.split()
                #print line
                if line[0].split("=")[1] == "strongsubj":
                    entry.setStrength(1) #strong
                else:
                    entry.setStrength(0) #weak
                entry.setText(line[2].split("=")[1])
                if len(both)>0 and entry == both[-1]:
                    flag = True
                entry.setPos(line[3].split("=")[1])
                if line[5].split("=")[1] == "negative":
                    entry.setPolarity(-1)
                else:
                    entry.setPolarity(1)
                if entry.getPolarity() == 1 and not flag:
                    positive.append(entry)
                    both.append(entry)
                elif not flag:
                    negative.append(entry)
                    both.append(entry)
    return [positive,negative,both]
    

def createNegated(subjfname):
    fp = open(subjfname,"r")
    df = open(subjfname+"-neg","w")
    for line in fp:
        df.write(line)
        parts = line.split()
        newpol = parts[5].split("=")[1]
        if newpol == "negative":
            newpol = "positive"
        elif newpol == "positive":
            newpol = "negative"
        newtext = "not-"+parts[2].split("=")[1]
        df.write(parts[0]+" "+parts[1] + " word1="+newtext+ " " + parts[3] +" "+ parts[4] + " priorpolarity="+newpol+"\n")
    df.close()
    fp.close()


def main():
    name = "subjclues.tff"
    createNegated(name)
    results = weibe(name,True)


if __name__=="__main__":
    main()




