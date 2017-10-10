#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import jieba
import os
import w2vmodel

# following execution of demo-0.py
def makemodels(folder, modelpath):
    os.system("mkdir models")
    w2vmodel.make_w2v(folder, modelpath)
makemodels("segmentedfordemos", "models/textw2v.model")
# model结果会在"models"文件夹的"textw2v.model"文件中。
