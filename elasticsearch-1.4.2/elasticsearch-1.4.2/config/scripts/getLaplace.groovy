def termfreq = 0
def docLength = 0
def score = 0
for (term in query)
   {
    termfreq = _index[field][term].tf()
    docLength = doc['doclength'].value
    score = score + log((termfreq+1)/(docLength+vocabSize))
    }
score;