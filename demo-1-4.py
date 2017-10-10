#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import jieba
import os
import d2vmodel
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
d2vmodel.load_d2v("models/textd2v.model")