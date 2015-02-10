def termfreq = 0
def docLength = 0
def score = 0
def k1 = 1.2
def k2 = 100
def b = 0.75
def querytermfreq = query.countBy{it}

for (term in query)
   {
    termfreq = _index[field][term].tf()
    docfreq = _index[field][term].df()
    docLength = doc['doclength'].value
    score = score + (log((ndocs + 0.5)/(docfreq + 0.5))*((termfreq+k1*termfreq)/(termfreq + (k1*((1-b)+(b*docLength/avgLength)))))*((querytermfreq[term]+k2*querytermfreq[term])/(querytermfreq[term]+k2)))
    }
score;