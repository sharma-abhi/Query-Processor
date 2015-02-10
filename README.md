### Introduction
This is a query processor i built in Python, using elastic search for parsing documents.

Objective is to parse 84000 documents and compute the best 100 relevant documents for each of the 25 queries using custom scoring models.

Implemented using 
- Python
- Groovy
- Elastic Search

I used the following 5 models for calculating scores(using custom groovy scripts).
- Okapi TF
- TF-IDF
- Okapi BM
- Unigram LM with Laplace Smoothing
- Unigram LM with Jelinek-Mercer Smoothing

### Setup
- Install Elastic search.
- Place the contents of the config folder in  `elasticsearch-1.4.2\elasticsearch-1.4.2` in the respective elastic search folder.
- start the service using the command: 
``
service start
``
- Open Sense through Marvel plugin `localhost:9200/_plugin/marvel/`
- Run the Sense commands provided in the `Sense setup.txt`
- Run the python file `create_index.py` to create the indexes
and `computequery.py` to query the documents.
- 5 output files for each of the 5 models would be created in a `Results` folder.
