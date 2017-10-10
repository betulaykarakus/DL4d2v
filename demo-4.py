# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding("utf8")
import jieba
import os
import w2vmodel


def makemodels(folder, modelpath):
    os.system("mkdir models")
    return w2vmodel.make_w2v(folder, modelpath)


model = makemodels("segmentedfordemos", "models/textw2v.model")
lines = open("models/textw2v.model").readlines()


print w2vmodel.topn_sim_word(u"血糖水平", 5, model)