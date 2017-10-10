#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import w2vmodel
#import uniout
import jieba
import os
import gensim
import logging
import gensim.corpora.dictionary
from jieba.analyse import extract_tags
from gensim.models.keyedvectors import KeyedVectors
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
        # self.dirname = MySentences

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            # "fname "==all files in folder
            for line in open(os.path.join(self.dirname, fname)):
                # "line " == each line in all files
                yield line.decode("utf8").split()
def getsamples():
    list = open("stereowords.txt").readlines()
    samples = {}
    for x in list:
        y = x.split()
        if len(y)>1:
            samples[y[0]] = y[1]
    return samples
def gettopics():
    topics = open("topicslist.txt").read().split()
    return topics
def gethighfreq():
    highfreqwords = []
    for axtxt in os.listdir("segmented2"):
        #os.system("rm -r tmpmodeldir")
        # extract top10 freq wds of each file
        text = open("segmented2/"+axtxt).read()
        for x in extract_tags(text, topK=20, withWeight=True):
            highfreqwords.append(x[0])
    #print "highfreqwords: ", highfreqwords

    return highfreqwords
def matchtopics(words, samples):
    topics = {}
    model = w2vmodel.load_w2v()
    for wd in words:
        wdlist = {}
        #print w2vmodel.sim_btw_ws('二甲双胍'.encode("utf8"), '糖尿病'.encode("utf8"), model)
        for k,v in samples.iteritems():
            try:
                wdlist[k] = w2vmodel.sim_btw_ws(k.decode("utf-8"), wd.decode("utf-8"), model)
            except:
                wdlist[k] = 0
            #print "wdlist[k]", wdlist[k]
            #print "k", k
            #print "wd", wd
        maxsim = 0
        for sampleword, similarity in wdlist.items():
            if similarity > maxsim:
                maxsim = similarity
        for k, v in wdlist.items():
            if v == maxsim:
                topic = samples[k] # topic for wd
                topics[wd] = topic
    return topics
def modifytopics(topics):
    os.system("mkdir lists")
    for k,v in topics.iteritems():
        f = open("lists/"+v.decode("utf8"), "a")
        f.write(k.decode("utf-8")+" ")
        f.close()
    print "Please check words in lists/"

def drawchart(types, topics):
    chartlengths = {}
    for axtxt in os.listdir("segmented2"):
        text = open("segmented2/"+axtxt).read()
        docradar = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in extract_tags(text, topK = 20, withWeight = True):
            x_topic = topics[x[0]]
            x_weight = x[1]
            for i in range(0, len(types)):
                if types[i] == x_topic:
                    docradar[i] += x_weight
        sum = 0
        for m in range(0, len(docradar)):
            sum += docradar[m]
        for m in range(0, len(docradar)):
            docradar[m] = docradar[m]*100.0/sum
        chartlengths[axtxt] = docradar
    return chartlengths
def readchartdata(chartlengths):
    for k1, v1 in chartlengths.iteritems():
        print "\t\t\t{\n\t\t\t\tvalue: ["+str(v1[0])+",",
        for i in range(1, len(v1)-1):
            print str(v1[i])+",",
        print str(v1[len(v1)-1])+"],\n\t\t\t\tname:",
        print "\'"+ k1[:-4] + "\'\n\t\t\t},\n"


    for i in range(1, 81):
        print "\'a_"+str(i)+"\',",
def main():
    samples = getsamples()
    types = gettopics()
    highfreqwords = gethighfreq()
    topics = matchtopics(highfreqwords, samples)
    ftopic = open("words_topics.txt", "w")
    for k, v in topics.iteritems():
        ftopic.write(k.decode("utf-8")+"\t"+v.decode("utf-8")+"\n")
    ftopic.close()
    #modifytopics(topics)
    chartlengths = drawchart(types, topics)
    fchart = open("chartlengths.txt", "w")
    for k1, v1 in chartlengths.iteritems():
        fchart.write(k1+"\t")
        for j in range(0, len(v1)):
            fchart.write(str(v1[j])+", ")
        fchart.write("\n")
    fchart.close()
    readchartdata(chartlengths)


main()