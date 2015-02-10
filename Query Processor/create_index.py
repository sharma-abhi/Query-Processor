from elasticsearch import Elasticsearch    
from os import listdir
import re
import string

es = Elasticsearch()

filepath = 'Query Processor/AP89_DATA/AP_DATA/ap89_collection'
filenames = listdir(filepath)

stopFilePath = "elasticsearch-1.4.2/elasticsearch-1.4.2/config"
stopFileName = 'stoplist.txt'
fstop = open(stopFilePath+"/"+stopFileName)
stopFileData = fstop.readlines()

# little cleaning up the stop list data
stopFileData = [x.replace("\n",'') for x in stopFileData]

for file in filenames:
    f = open(filepath+"/"+file)
    filedata = f.readlines()
    textBool = False
    textString = ""
    for line in filedata:
        if line.startswith("<DOCNO>"):
            docNo = line[8:21]
        if line.startswith("</TEXT>"):
            textBool = False
        if textBool == True:
            textString += line
        if line.startswith("<TEXT>"):
            textBool = True       
        if line.startswith("</DOC>"):
            textString = textString.replace("\n"," ")
            
            tlist = textString.split()
            slist=[]
            for i in range(len(tlist)):
                if tlist[i] in stopFileData:
                    slist.append('')
                else:
                    slist.append(tlist[i])
            textString = ' '.join(slist)
            # Converting to lowertext
            textString = textString.lower()
            # Removing punctuations from query
            for p in string.punctuation:
                if p != '_' and p!='-' and p!='\'':
                    textString = textString.replace(p," ")
            textString = textString.replace("  "," ")        
            docLength = len(textString.split())
            doc = {
                    'docno' : docNo,
                    'text': textString,
                    'doclength': docLength
                    }
            res = es.index(index="ap_dataset", doc_type='document', id=docNo, body=doc)

            textBool = False
            textString = ""
    f.close()
    fstop.close()
    