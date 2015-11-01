import commands
from sys import argv
import os
dir = argv[1]

files = os.listdir(dir)

for file in files:
    fileName = dir+'/'+file
    (status, output) = commands.getstatusoutput("curl 'http://localhost:8983/solr/collection1/update?wt=json' --data-binary @"+fileName+" -H 'Content-type:application/json'")
    print(status, output)
