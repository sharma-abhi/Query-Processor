def termfreq = 0
def docLength = 0
def score = 0
for (term in query)
   {
    termfreq = _index[field][term].tf()
    totaltermfreq = _index[field][term].ttf()
    docLength = doc['doclength'].value
    score = score + log((lamb*(termfreq/docLength))+((1-lamb)*(totaltermfreq/sumdoclength)))
    }
score;