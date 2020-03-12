import json
import math
import operator


def main():
    dataFile=open("dataset.json","r")
    jsonData=dataFile.read()
    #stopFile=open("stopwords.txt","r")
    #stopList=stopFile.read().split()
    dataset=json.loads(jsonData)
    tfPositive={}
    tfNegative={}
    counterPositive=0
    counterNegative=0
    for line in dataset:
        if dataset[line]=="0":
            output=tfNegative
            counterNegative+=1
        else:
            output=tfPositive
            counterPositive+=1
        #print(str(counterPositive)+" "+str(counterNegative))
        line=line.lower()
        for char in line:
            if char in ",?.!/;:":
                line=line.replace(char,"")
        splitLine=line.split()
        for word in splitLine:
            if 1==1:#if word not in stopList:
                if word not in output:
                    output[word]=0
                output[word]+=1
    for entry in tfPositive:
        tfPositive[entry]/=counterPositive
    for entry in tfNegative:
        tfNegative[entry]/=counterNegative
    tf=tfPositive
    for x in tfNegative:
        if x in tfPositive:
            tfPositive[x]-=tfNegative[x]
        else: tfPositive[x]=tfNegative[x]*(-1)
    for x in tf:
        tf[x]=math.floor(tf[x]*10000)/100
    tf=sorted(tf.items(),key=operator.itemgetter(1))
    jsonString="{"
    for x in tf:
        jsonString+="\n\t\""+x[0]+"\":\""+"0"+"\","
    jsonString=jsonString[:-1]
    jsonString+="\n}"
    save=open("tf.json","w+")
    save.write(jsonString)
    save.close
main()
