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
# Assignment 1 Part B             #
###################################

#from pocheng_Assignment_1A import *
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

def getFilesInfo(file1, file2):
    filename1 = file1
    filename2 = file2
    file1Start = timeit.default_timer()
    tokens1 = computeWordFrequencies(tokenize(filename1))
    file1End = timeit.default_timer()
    file2Start = timeit.default_timer()
    tokens2 = computeWordFrequencies(tokenize(filename2))
    file2End = timeit.default_timer()
    return [list(tokens1.keys()), list(tokens2.keys()), file1End-file1Start, file2End-file2Start]

def compareTwoTokens(tokens1, tokens2):
    compareList = list(set(tokens1) & set(tokens2))
    return compareList

def printCommonTokens(file1, file2):
    count = 0
    filesInfo = getFilesInfo(file1, file2)
    compareStart = timeit.default_timer()
    compareList = compareTwoTokens(filesInfo[0], filesInfo[1])
    compareEnd = timeit.default_timer()
    count = len(compareList);
    #print("Common words: {common}".format(common=compareList))
    print("Total common tokens: {num}".format(num=count))
    print("\nTotal time for processing file 1's tokens:\n{time}".format(time=filesInfo[2]))
    print("\nTotal time for processing file 2's tokens:\n{time}".format(time=filesInfo[3]))
    print("\nTotal time for comparing file 1's tokens and file 2's tokens:\n{time}\n".format(time=compareEnd-compareStart))

def main():
    if len(sys.argv) != 3:
        print("Too few or too many arguments!")
        print("Input only 2 file!")
        sys.exit(0)
    else:
        checkFileExists(sys.argv[1])
        checkFileExists(sys.argv[2])
        printCommonTokens(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
