# encoding=utf8
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import os
import gensim
import logging
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from pprint import pprint
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def practice():
    model = make_d2v()
    output_doc_vec(model)
    find_sim_docs(model)
def make_d2v():

    articles = []
    ids = []
    docs = []

    for i in range(1, len(os.listdir("segmented/"))+1):
        article = open("segmented/a_" + str(i) + ".txt").read().split()
        articles.append(article)
        ids.append(str(i))
        docs.append(TaggedDocument(article, [str(i)]))

    # initialize a model
    model = Doc2Vec(size=200, window=5, min_count=1, workers=10, alpha=0.025, min_alpha=0.01, dm=0)
    # print model
    # build vocabulary
    # 必须有这行才能有下一行
    model.build_vocab(docs)

    model.save("models/d2v.model")
    # train this model
    model.train(docs, total_examples=len(docs), epochs=100)
    return model


def load_d2v():
    # get the trained document vector, and most similar articles
    # (after training, the results should be correct)

    model2 = gensim.models.Doc2Vec.load("models/d2v.model")
    return model2

def output_doc_vec(model2):
    docvec2 = model2.docvecs[9]

    docvecsyn2 = model2.docvecs.doctag_syn0[9]

    print(docvec2[:5])
    print(docvecsyn2[:5])
def find_sim_docs(model2):
    docsim2 = model2.docvecs.most_similar(9)

    print(docsim2[:2])
    #print ids[9]
