#!/usr/bin/python3
mypath = "/Users/rphuyal"
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
