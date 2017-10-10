#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import jieba
import os
import d2vmodel
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

def make_d2v(fromdir, topath):

    articles = []
    ids = []
    docs = []
    i = 0
    for filei in os.listdir(fromdir+"/"):
        article = open(fromdir+"/" + filei).read().split()
        articles.append(article)
        ids.append(str(i))
        docs.append(TaggedDocument(article, [str(i)]))
        i +=1

    # initialize a model
    model = Doc2Vec(size=200, window=5, min_count=1, workers=10, alpha=0.025, min_alpha=0.01, dm=0)
    # print model
    # build vocabulary
    # 必须有这行才能有下一行
    model.build_vocab(docs)

    model.save(topath)
    # train this model
    model.train(docs, total_examples=len(docs), epochs=100)
    return model

make_d2v("segmentedfordemos", "models/textd2v.model")
# d2vmodel结果会在"models"文件夹的"textd2v.model"文件中。
# 此文件为BINARY文件，不能直接阅读，但我们可以在其他DEMO中运用此模型得到关于语料库的信息。