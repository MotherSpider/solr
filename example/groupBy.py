#!/usr/bin/python


import os
import sys
import json

def readDir(dir):
	jsonList = []
	fileNames = os.listdir(dir)
	for fileName in fileNames:
		j = json.loads(open(dir+'/'+fileName, 'rU').read())
		jsonList.append(j)

	return jsonList

def groupBy(attr, jsonList, identifier):
	hash = {}
	for j in jsonList:
		key = j["add"]["doc"].get(attr, None)
		if key is not None:
			value = hash.get(key, [])
			value.append(j["add"]["doc"].get(identifier, ''))
			hash[key] = value
	return hash

def groupByLatLon(jsonList, identifier):
	hash = {}
	for j in jsonList:
		k1 = j["add"]["doc"].get("geonames_address.geo.lat", None)
		k2 = j["add"]["doc"].get("geonames_address.geo.lon", None)
		key = None
		if k1 is not None and k2 is not None:
			key = str(round(float(k1), 1)) + ", " + str(round(float(k2), 1))

		if key is not None:
			value = hash.get(key, [])
			value.append(j["add"]["doc"].get(identifier, ''))
			hash[key] = value
	return hash

def write(hash, attr):
	f = open('group-by-'+attr+".txt", 'w')
	SPACE = ' '
	NEW_LINE = '\n'
	for key in hash.keys():
		f.write(key+SPACE)
		for value in hash[key]:
			f.write(str(value)+SPACE)
		f.write(NEW_LINE)


def main():
	args = sys.argv[1:]
	if len(args) < 3:
		print('usage: ./groupBy.py json-directory <group-by-attr>|lat-lon identifier')
		exit(0)

	jsonList = readDir(args[0])
	attr = args[1]
	identifier = args[2]


	if attr == 'lat-lon':
		hash = groupByLatLon(jsonList, identifier)
	else:
		hash = groupBy(attr, jsonList, identifier)

	write(hash, attr)


if __name__ == '__main__':
	main()









