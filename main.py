import json

class Neuron:
    def __init__(self,s,w):
        self.word=s
        self.weight=float(w)
def prepare(sentence):
    sentence=sentence.lower()
    for c in sentence:
        if c in ",?.!/;:":
            sentence=sentence.replace(c,"")
    return sentence
def calculate(network,sentence):
    words=sentence.split()
    neurons=[]
    for word in words:
        if word in network:
            neurons.append(network[word])
    outcome=0
    for n in neurons:
        outcome+=float(n.weight)
    return outcome
def check(network,sentence,outcome,dataset):
    if sentence not in dataset:
        return "idk"
    else:
        if dataset[sentence]=="0" and outcome<0:
            return "good"
        elif dataset[sentence]=="1" and outcome>0:
            return "good"
        else:
            return "bad"
def test(network,dataset):
    goodCounter=0
    badCounter=0
    for sentence in dataset:
        outcome=calculate(network,sentence)
        if check(network,sentence,outcome,dataset)=="good":
            goodCounter+=1
        elif check(network,sentence,outcome,dataset)=="bad":
            badCounter+=1
        else:
            nodataCounter+=1
    print("\tgood="+str(goodCounter))
    print("\tbad="+str(badCounter))
    print("\taccuracy="+str(goodCounter*100/(goodCounter+badCounter))+"%")
def sgn(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
def train(network,dataset):
    for sentence in dataset:
        expectation=1
        if dataset[sentence]=="0":
            expectation=-1
        sentence=prepare(sentence)
        while calculate(network,sentence)*expectation<=0:
            correct(network,sentence,expectation)
def correct(network,sentence,expectation):
    words=sentence.split()
    for word in words:
        if word in network:
            network[word].weight+=0.1*expectation
def main():
    dictionaryFile=open("data/tf.json","r")
    jsonData=dictionaryFile.read()
    dictionaryFile.close()
    dictionary=json.loads(jsonData)
    network={}
    for entry in dictionary:
        network[entry]=Neuron(entry,dictionary[entry])
    learnsetFile=open("data/learnset.json","r")
    jsonData=learnsetFile.read()
    learnsetFile.close()
    learnset=json.loads(jsonData)
    testsetFile=open("data/testset.json","r")
    jsonData=testsetFile.read()
    testsetFile.close()
    testset=json.loads(jsonData)

    print("before:")
    test(network,learnset)
    print("after:")
    train(network,learnset)
    test(network,learnset)
    print("testing:")
    test(network,testset)
    
main()
