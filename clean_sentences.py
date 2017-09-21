#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import jieba
import os
def getmatchlist():
    matchlist = {}
    fm = open("matchlist.txt", "r")
    for eachline in fm.readlines():
        tmplist = eachline.split(".txt\t")
        matchlist[tmplist[0]+".txt"] = tmplist[1]
    fm.close()
    return matchlist


def fenju():
    punc = "。？！；：:;!?\n\r\b\t"
    flist = os.listdir("dbfiles/")
    jieba.load_userdict("userdict")
    puncl = open("puntuation.txt").read().replace('\n', '')
    for n in range(1, len(flist)+1):
        # split sentences in numbered/n.txt and save in sentences
        booleanval = 0
        line2 = ""
        for line in open("dbfiles/a_" + str(n) + ".txt").readlines():
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
            .replace(u"II 型糖尿病", u"二型糖尿病").replace(u"1型 糖尿病", u"一型糖尿病") \
            .replace(u"1型糖尿病", u"一型糖尿病").replace(u"I 型 糖尿病", u"一型糖尿病") \
            .replace(u"I 型糖尿病", u"一型糖尿病")

        for ch in puncl.decode("utf8"):
           line2 = line2.replace(ch+u' ', u'')


        open("segmented/a_" + str(n) + ".txt", "w").write(line2)


def main1():
    matchlist = getmatchlist()
    os.system("mkdir segmented")
    try:
        fenju()
    except:
        print "fenju failed"
    return matchlist

#main1()




