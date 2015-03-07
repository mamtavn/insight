import os, os.path
import sys
import re

#default files and directories
DEFAULT_INPUT_DIR = "wc_input"
DEFAULT_OUTPUT_DIR = "wc_output"
DEFAULT_WC_FILE = "wc_result.txt"
DEFAULT_MEDIAN_FILE = "med_result.txt"

# leading/trailing characters to be stripped off from a word
STRIP_CHARS = ',:?.!;()"\''

# get all the files under a given directory
def getFiles(dirName):
        files = []
        absoluteName = os.path.abspath(dirName)

        if os.path.isdir(absoluteName):
                for f in os.listdir(absoluteName):
                        f = absoluteName + os.path.sep + f
                        if os.path.isfile(f):
                                files.append(f)
        else:
                files.append(absoluteName)
        return files

# given an array returns the median
def getMedian(numArray):
        # sort the array for finding the median
        median = -1
        sortedArray = sorted(numArray)
        size = len(sortedArray)      

        midsize = int(size/2); 
        if (size % 2):
                # for odd numbered elements, pick the middle one
                median = sortedArray[midsize]
        else:
                # for even numbered elements, average them out
                median = (sortedArray[midsize-1] + sortedArray[midsize])/2
                
        return median

# for a given filename returns the words and the number of occurences
def getWordCount(fname):
        mediancount = []
        try:
                f = open(fname, "r")
                # a dict with k,v pair of word,count
                wordlist = {}
                # total words on a given line for getting running median
                wordlinecount = []
                
                data = f.readlines()
                for line in data:
                        # taking care of blank lines 
                        if line.strip():
                                words = line.split()
                                actualwordcount = 0

                                for word in words:
                                        # convert the word to lowercase and strip the leading/trailing punctuation
                                        if re.search('[a-zA-Z0-9]+',word):
                                                actualwordcount += 1
                                                lcword = word.lower().strip(STRIP_CHARS)
                                                lcword = lcword.replace('-','')
                                                if lcword not in wordlist:
                                                        # first time adding the word
                                                        wordlist[lcword] = 1
                                                else:
                                                        # word already there, so increase the count
                                                        wordlist[lcword] += 1

                f.close()
                return(wordlist)
        except:
                raise
                    
def getRunningMedian(dirName):
        try:
                #holds the running median
                mediancount = []
                # total words on a given line for getting running median
                wordlinecount = []
                
                # get all the files that need to be parsed
                filenames = sorted(getFiles(dirName))
                for fname in filenames:
                        print("----processing file ", fname)
                        f = open(fname, "r")

                        data = f.readlines()
                        for line in data:
                                # taking care of blank lines
                                actualwordcount = 0
                                if line.strip():
                                        words = line.split()
                                        for word in words:
                                                # a word should have atleast a letter or a number (i think)
                                                if re.search('[a-zA-Z0-9]+', word):
                                                        actualwordcount += 1
                                wordlinecount.append(actualwordcount)
                                median = getMedian(wordlinecount)
                                print("----", actualwordcount)
                                mediancount.append(median)
                        f.close()
                return(mediancount)
        except:
                raise
        
