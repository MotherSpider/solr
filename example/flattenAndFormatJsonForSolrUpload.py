#!/usr/bin/python

import sys
import json
import os

def flattenDict(d, result=None):
    if result is None:
        result = {}
    for key in d:
        value = d[key]
        if isinstance(value, dict):
            value1 = {}
            for keyIn in value:
                value1[".".join([key,keyIn])]=value[keyIn]
            flattenDict(value1, result)
        elif isinstance(value, (list, tuple)):
            for indexB, element in enumerate(value):
                if isinstance(element, dict):
                    value1 = {}
                    index = 0
                    for keyIn in element:
                        newkey = ".".join([key,keyIn])
                        value1[".".join([key,keyIn])]=value[indexB][keyIn]
                        index += 1
                    for keyA in value1:
                        flattenDict(value1, result)
        else:
            result[key]=value
    return result

def appendMetaDataToFile(j):
    text = json.dumps(j);
    text = "{\"add\":{\"doc\":"+text+"}}"
    return text

def writeJsonToFile(fileName, text):
    open(fileName, 'w').write(text);

def main():
    args = sys.argv[1:];
    dir = args[0]
    newDir = args[1]
    fileNames = os.listdir(dir);
    for fileName in fileNames:
            text = open(dir+'/'+fileName, 'r').read()
            text = appendMetaDataToFile(flattenDict(json.loads(text)))
            writeJsonToFile(newDir+"/"+fileName, text);


if __name__ == '__main__':
    main()

    



    
