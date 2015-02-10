### Introduction
This is a query processor i built in Python, using elastic search for parsing documents.This also compares different scoring models and outputs the documents according to Rank.
Implemented using 
-- Python
-- Groovy
-- Elastic Search

Setup
Install Elastic search and start the service using the command: 
``
service start
``
open Sense through Marvel plugin `localhost:9200/_plugin/marvel/`
Run the Sense commands provided in the `Sense setup.txt`

Run the python file `create_index.py` to create the indexes
and `computequery.py` to query the documents.
