# Copyright 2017 Pok On Cheng
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

###################################
# Pok On Cheng (pocheng) 74157306 #
# CompSci 121                     #
# Information Retrieval (ugrad)   #
# Assignment 1 Part A             #
###################################

import operator
import os
import re
import sys
import timeit

def openFileRead(filename):
    try:
        with open(filename, encoding='ASCII') as fread:
            contents = fread.readlines()
            print("File ({TextFilePath}) is in 'ASCII' encoding!\n".format(TextFilePath=filename))
            return contents
    except:
        print("File ({TextFilePath}) is not in 'ASCII' encoding!\n".format(TextFilePath=filename))
        sys.exit(0)

def checkFileExists(filename):
    if os.path.exists(filename):
        print("File ({TextFilePath}) exists!\n".format(TextFilePath=filename))
    else:
        print("File ({TextFilePath}) does not exist!\n".format(TextFilePath=filename))
        sys.exit(0)

def regexPatternCompile(pattern):
    regex = re.compile(pattern)
    return regex  

def tokenize(TextFilePath):
    tokens = []
    contents = openFileRead(TextFilePath)
    regex = regexPatternCompile('[- _\s\n,.<>/?:;\"\'\[\]{}\\\|`~!@#$%^&*()=\+]+')
    for row in contents:
        row = row.lower()
        temp = regex.split(row)
        tokens.extend(temp)
    return tokens

def computeWordFrequencies(tokens):
    dictTokens = {}
    found = False
    for token in tokens:
        if len(token) >= 1:
            if token == "":
                found = True
            if token in dictTokens.keys():
                dictTokens[token] += 1
            else:
                dictTokens[token] = 1
    if found:
        del dictTokens[""]
    return dictTokens

def printTokens(dictTokens):
    sortedTokens = sorted(dictTokens.items(), key=operator.itemgetter(1), reverse=True)
    print("Frequencies (\"key\": value):")
    for token in sortedTokens:
        print(("\"{tokenKey}\": {tokenValue}").format(tokenKey=token[0], tokenValue=token[1]))

def main():
    if len(sys.argv) != 2:
        print("Too few or too many arguments!")
        print("Input only 1 file!")
        sys.exit(0)
    else:
        checkFileExists(sys.argv[1])
        tokenizeStart = timeit.default_timer()
        tokens = tokenize(sys.argv[1])
        dictTokens = computeWordFrequencies(tokens)
        tokenizeEnd = timeit.default_timer()
        printStart = timeit.default_timer()
        printTokens(dictTokens)
        printEnd = timeit.default_timer()
        print("\nTotal time for processing tokens:\n{time}".format(time=tokenizeEnd-tokenizeStart))
        print("\nTotal time for printing tokens:\n{time}\n".format(time=printEnd-printStart))
        
if __name__ == "__main__":
    main()
