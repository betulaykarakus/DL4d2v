#encoding=utf8
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
print "特征词有:"
for i in range(1, len(lines)):
    print lines[i].split()[0],
print ""
print model[u"糖尿病"]
print model[u"糖尿病患者"]
print model[u"胰岛素"]