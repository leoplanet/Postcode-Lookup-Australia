#!/usr/bin/python -tt

import sys
import csv

def main():
  if len(sys.argv) == 2:
    # sys.argv[1] --> path
    filename = sys.argv[1]
    postcodedictionary = DictionarybyPostCode(filename)
    # sys.argv[2] --> postcode
    for key in postcodedictionary.keys():
      print "Post Code: ",key,"--> ",postcodedictionary[key]
  elif len(sys.argv) == 3:
    filename = sys.argv[1]
    postcodedictionary = DictionarybyPostCode(filename)
    postcode = sys.argv[2]
    if postcode in postcodedictionary.keys():
      print postcodedictionary[postcode]
    else:
      print "postcode not found"
  elif len(sys.argv) == 4:
    filename = sys.argv[1]
    postcodedictionary = DictionarybyPostCode(filename)
    postcode = sys.argv[2]
    locality = sys.argv[3].upper()
    if postcode in postcodedictionary.keys():
      if locality in postcodedictionary[postcode]:
        print "True"
      else:
        print "False"
    else:
      print "postcode not found"
  else:
    print "invalid arguments: plese run script with three arguments (filename/path, postcode, locality/suburb)"
  '''
  filename = sys.argv[1]
  localitydictionary = DictionarybyLocality(filename)
  for key in localitydictionary.keys():
      print "Locality: ",key,"--> ",localitydictionary[key]
  '''


def DictionarybyPostCode(filename):
  postcodes = {}
  f = open(filename,'rU')
  reader  = csv.reader(f, delimiter=",", quotechar="\"")
  for line in reader:
    #print line
    pcode = line[0]
    locality = line[1]
    #print pcode,locality
    if (pcode in postcodes.keys())==False:
      postcodes[pcode] = [locality]
    else:
      #print postcodes[pcode]
      postcodes[pcode].append(locality)
      #print postcodes[pcode]
  return postcodes

def DictionarybyLocality(filename):
  localities = {}
  f = open(filename,'rU')
  reader  = csv.reader(f, delimiter=",", quotechar="\"")
  for line in reader:
  #print line
    pcode = line[0]
    locality = line[1]
    #print pcode,locality
    if (locality in localities.keys())==False:
      localities[locality] = [pcode]
    else:
      #print postcodes[pcode]
      localities[locality].append(pcode)
      #print postcodes[pcode]
  return localities

if __name__ == '__main__':
  main()
