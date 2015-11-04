import commands
from sys import argv
import os
dir = argv[1]

files = os.listdir(dir)
i = 1
for file in files:
    fileName = dir+'/'+file
    (status, output) = commands.getstatusoutput("curl 'http://localhost:8983/solr/collection1/update?wt=json' --data-binary @"+fileName+" -H 'Content-type:application/json'")
    i += 1
    if i % 1000 == 0:
        print(i)
