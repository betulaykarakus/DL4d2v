# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding("utf8")
import jieba
import os
import d2vmodel
import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

# follow demo 1-4
model = d2vmodel.load_d2v("models/textd2v.model")
# 在textsfordemos文件夹中的五篇文章中，ID=2的文章最相似的三篇文章分别是
d2vmodel.find_sim_docs(model, 2, 3)
# 最相似的是ID=1的文章，相似度指数0.06758376955986023，其次是ID=0的文章，再其次是ID=4的文章