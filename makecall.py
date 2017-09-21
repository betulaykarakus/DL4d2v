# -*- coding: UTF-8 -*-
import sys
reload(sys)
import MySQLdb
import os
import uniout
sys.setdefaultencoding("utf-8")
import clean_sentences
import d2vmodel
import w2vmodel


# import other python files
# use: printFileNumber.function1(args)

# deprecated function to get matchlist
def unzip(corpuszipbao):
    txtlist = []
    # provided that corpus with xxx.zip format name
    os.system("unzip " + corpuszipbao + " -d corpus")
    os.system("unzip " + corpuszipbao)
    for root, dirs, files in os.walk("corpus", topdown = True):
        for x in files:
            txtlist.append(os.path.join(root, x))
            namelist.append(x)
        print "root=", root
    return txtlist
# deprecated function to assign nums to files
def assignNumsToFile(txtlist):
    fileNums = {}
    os.system("mkdir numbered")
    for n in range(1, len(txtlist) + 1):
        # move to folder "numbered"
        newpath = "numbered/" + str(n) + ".txt"
        print newpath
        oldpath = txtlist[n - 1]
        print oldpath
        os.rename(oldpath, newpath)
        # note into fileNums
        fileNums[str(n)+".txt"] = namelist[n - 1]
    return fileNums
def printmatchlist(matchlist):
    for k,v in matchlist.iteritems():
        print k.decode("utf8")+"\t"+v.decode("utf8")+"\n"

def main():
    # write files into folder dbfiles/
    # write matchlist in matchlist.txt and get
    os.system("python loadfromdb.py")
    matchlist = clean_sentences.main1()
    makemodels()
def makemodels():

    w2vmodel.make_w2v()
    d2vmodel.make_d2v()
    # to use wrd2vector to find similar words
    #d2vmodel.practice(doc1, doc2, doc3...)

main()
# global var here is visible in other files imported here
# the reverse NOT work




