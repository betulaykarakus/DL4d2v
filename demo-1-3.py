#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import jieba
import os
import w2vmodel
w2vmodel.load_w2v("models/textw2v.model")