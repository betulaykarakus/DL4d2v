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
def make_w2v(folder, modelpath):
    sentences = MySentences(folder)
    model = gensim.models.Word2Vec(sentences, size=200, window=5, min_count=5, workers=10)
    model.wv.save_word2vec_format(modelpath, binary = False)
    return model

def load_w2v(modelname):
    model = KeyedVectors.load_word2vec_format(modelname, binary = False)
    return model

def topn_sim_word(w1, topn, model):
    return model.similar_by_word(w1, topn)

def sim_btw_ws(w1, w2, model):
    return model.similarity(w1, w2)
#for line in open("models/w2v.model").readlines():
    #print line.split()[0],

'''
model = load_w2v('models/w2v.model')
#print sim_btw_ws('二甲双胍'.encode("utf-8"), '糖尿病'.encode("utf-8"), model)
#print sim_btw_ws('二甲双胍'.encode("utf8"), '糖尿病'.encode("utf8"), model)



#print sim_btw_ws('二甲双胍'.encode("ascii"), '糖尿病'.encode("ascii"), model)
#print sim_btw_ws('二甲双胍'.decode("ascii"), '糖尿病'.decode("ascii"), model)
#print sim_btw_ws('二甲双胍'.decode("utf-8"), '糖尿病'.decode("utf-8"), model)
#print sim_btw_ws('二甲双胍'.decode("utf8"), '糖尿病'.decode("utf8"), model)


print sim_btw_ws('二甲双胍'.encode("ascii"), '糖尿病'.encode("ascii"), model)
print sim_btw_ws('二甲双胍'.encode("ascii"), '糖尿病'.encode("ascii"), model)

print sim_btw_ws('二甲双胍'.encode("utf8"), '糖尿病'.encode("utf8"), model)
print sim_btw_ws('二甲双胍'.encode("utf8"), '糖尿病'.encode("utf8"), model)
print sim_btw_ws('二甲双胍'.encode("utf8"), '糖尿病'.encode("utf8"), model)
print sim_btw_ws('二甲双胍'.encode("utf8"), '糖尿病'.encode("utf8"), model)
print sim_btw_ws('二甲双胍'.encode("utf8"), '糖尿病'.encode("utf8"), model)



print topn_sim_word(u"肥胖", 20, model)


print topn_sim_word(u"妊娠糖尿病", 20, model)
print topn_sim_word(u"一型糖尿病", 20, model)
print topn_sim_word(u"二型糖尿病", 20, model)
print topn_sim_word(u"营养", 20, model)
print topn_sim_word(u"肾病", 20, model)
print topn_sim_word(u"糖尿病足", 20, model)
print topn_sim_word(u"眼病", 20, model)
print topn_sim_word(u"心血管病", 20, model)
print topn_sim_word(u"低血糖", 20, model)
print topn_sim_word(u"性功能障碍", 20, model)
print topn_sim_word(u"降糖药物", 20, model)


#print model.similar_by_word(u"糖尿病患者", topn=10)

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
