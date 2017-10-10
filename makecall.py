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
import jieba
from jieba.analyse import extract_tags

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
def collect_highfreq_wds_to(fromdir, todir):
    outf = open(todir, "w")
    for x in os.listdir(fromdir):
        if os.path.isfile(fromdir + "/"+x):
            text = open(fromdir + "/"+x).read()
            #for y in extract_tags(text, withWeight=True):
                #outf.write(y[0]+" ")
            for y in extract_tags(text, topK=100, withWeight=True):
                print y[0]
                print y[1]
        outf.write("\n")
    outf.close()
def makemodels(folder, modelpath):
    os.system("mkdir models")
    w2vmodel.make_w2v(folder, modelpath)
    #d2vmodel.make_d2v()
    # to use wrd2vector to find similar words
    #d2vmodel.practice(doc1, doc2, doc3...)
def main():
    # write files into folder dbfiles/
    # write matchlist in matchlist.txt and get
    os.system("python loadfromdb.py")
    matchlist = clean_sentences.main1()
    makemodels()


main()
makemodels("segmented/", "models/w2v.model")
#collect_highfreq_wds_to("filetmp/", "tmpstats.txt")
# global var here is visible in other files imported here
# the reverse NOT work




