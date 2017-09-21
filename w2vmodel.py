#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import uniout
import jieba
import os
import gensim
import logging
import gensim.corpora.dictionary
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
def make_w2v():
    sentences = MySentences("segmented/")
    model = gensim.models.Word2Vec(sentences, size=200, window=5, min_count=5, workers=10)
    os.system("mkdir models")
    model.wv.save_word2vec_format("models/w2v.model", binary = False)

def load_w2v():
    model = KeyedVectors.load_word2vec_format('models/w2v.model', binary = False)

def topn_sim_word(w1, topn):
    return model.similar_by_word(w1, topn)

def sim_btw_ws(w1, w2):
    return model.similarity(w1, w2)


'''
topn_sim_word(u"糖尿病患者", topn=10)
print model.similar_by_word(u"糖尿病", topn=10)

print model.similar_by_word(u"胆固醇", topn=10)
#print word_vectors.similar_by_vector(0.11675514280796051, topn=3)
print model.similarity(u"糖尿病患者", u"患者")
print model.similarity(u"甘油三酯", u"胆固醇")

#print gensim.models.word2vec.score_sg_pair(model, word, word2)
#print word_vectors[u"糖尿病患者"]
#print word_vectors.wv[u"糖尿病患者"]
#print word_vectors[u"糖尿病"]
#print model.wv[u"糖尿病"]
'''