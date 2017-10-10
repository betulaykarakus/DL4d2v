#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import jieba
import os
import clean_sentences

def fenju(foldername):
    punc = "。？！；：:;!?\n\r\b\t"
    flist = os.listdir(foldername)
    jieba.load_userdict("userdict")
    puncl = open("puntuation.txt").read().replace('\n', '')
    for axtxt in flist:
        # split sentences in numbered/n.txt and save in sentences
        booleanval = 0
        line2 = ""
        for line in open(foldername+"/" + axtxt).readlines():
            line = line.decode('UTF8').replace(u'\u3000', u'\n').replace(u'\u0020', u'\n') \
            .replace(u'\uFEFF', u'\n').replace(u'\u00A0', u'\n')
            if line == "":
                continue
            else:
                for c in line:
                    if c in punc and booleanval == 0:
                        line2 += "\n"
                        booleanval = 1
                    elif c in punc and booleanval == 1:
                        continue
                    else:
                        line2 += c
                        booleanval = 0

        segs = jieba.cut(line2, cut_all = False)
        line2 = (" ".join(segs)).replace(' \n ', '\n').replace(u"2型 糖尿病", u"二型糖尿病") \
            .replace(u"2型糖尿病", u"二型糖尿病").replace(u"II 型 糖尿病", u"二型糖尿病") \
            .replace(u"II 型糖尿病", u"二型糖尿病").replace(u"2 型糖尿病", u"二型糖尿病") \
            .replace(u"1型 糖尿病", u"一型糖尿病").replace(u"1 型糖尿病", u"一型糖尿病") \
            .replace(u"1型糖尿病", u"一型糖尿病").replace(u"I 型 糖尿病", u"一型糖尿病") \
            .replace(u"I 型糖尿病", u"一型糖尿病")

        for ch in puncl.decode("utf8"):
           line2 = line2.replace(ch+u' ', u'')


        open("segmentedfordemos/" + axtxt[:-4]+"_segmented.txt", "w").write(line2)

fenju("textsfordemos")
# 分句和分词结果会在"segmentedfordemos"文件夹的"a_1fordemo_segmented.txt"文件中。