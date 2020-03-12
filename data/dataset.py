def main(fileList):
    dataset={}
    for file in fileList:
        file="datasources/"+file
        print(file)
        f=open(file,"r")
        string=f.readlines()
        for line in string:
            x=line.split("\t")
            if x[0] not in dataset:
                x[1]=x[1].replace("\n","")
                dataset[x[0]]=x[1]    
    json="{"
    for x in dataset:
        json+="\n\t\""+x+"\":\""+dataset[x]+"\","
    json=json[:-1]
    json+="\n}"
    save=open("dataset.json","w+")
    save.write(json)
    save.close

main(["amazon_cells_labelled.txt","imdb_labelled.txt","yelp_labelled.txt"])
