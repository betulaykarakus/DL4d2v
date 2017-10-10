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
# 在textsfordemos文件夹中的五篇文章中，ID=0,1,2,3,4的文章的向量表示分别是：

d2vmodel.output_doc_vec(model, 0)
d2vmodel.output_doc_vec(model, 1)
d2vmodel.output_doc_vec(model, 2)
d2vmodel.output_doc_vec(model, 3)
d2vmodel.output_doc_vec(model, 4)