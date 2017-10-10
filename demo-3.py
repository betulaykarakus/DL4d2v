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
# 比较词语间相似度：
print w2vmodel.sim_btw_ws(u"糖尿病", u"血红蛋白", model)
print w2vmodel.sim_btw_ws(u"糖尿病", u"糖尿病患者", model)
print w2vmodel.sim_btw_ws(u"糖尿病", u"血糖", model)