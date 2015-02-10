def termfreq = 0
def docLength = 0
def score = 0
for (term in query)
   {
    termfreq = _index[field][term].tf()
    docLength = doc['doclength'].value
    score = score + (termfreq/(termfreq+0.5+(1.5*(docLength/avgLength))))
    }
score;