#!/bin/bash
for filename in ./flattenedJson/*.*; do
    curl 'http://localhost:8983/solr/collection1/update?wt=json' --data-binary @$filename -H 'Content-type:application/json'
done