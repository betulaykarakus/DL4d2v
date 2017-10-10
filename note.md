
# 所有文件的作用
## userdict：
分词字典。
## puntuation.txt
分句和分词所需标点和特殊符号。
## stereowords.txt:
每一行以“样词 类别”格式的每一类词语样例，由w2v&d2v模型提供的词语相似度生成。在makecall.py调用创建模型的d2vmodel.py和w2vmodel.py之后，可以使用w2vmodel.py和d2vmodel.py中利用已创建模型得到相似度的方法来生成这个txt文件。
## topicslist.txt：
认为需要的话题列表分行文件。
## loadfromdb.py:
（1）从数据库取得文章

（2）把文章标题改成有顺序的编号，存入文件夹dbfiles

（3）获得每篇文章的原标题和现有编号对应表，记录在matchlist.txt中。

## clean_sentences.py:
（1）获得matchlist

（2）所有dbfiles中的文章，分句，并且分词之后，以同样名称存入文件夹segmented中。

## givewordstype.py:
（1）把stereowords.txt中样词和对应类别存入字典samples

（2）从topicslist.txt得到话题，即文章所对应的方向类型。

（3）有选择的从segmented文件夹中选取一部分文件到segmented2文件夹，对其中的文件生成雷达图。（这一步可以将所有segmented2直接改成segmented）

（4）根据每篇文章高频词所在类别决定每篇文章在每个方向上的比例分布，得到可以画雷达图的数据。
## w2vmodel.py和d2vmodel.py：
（1）创建两种模型

（2）SAVE & LOAD 两种模型

（3）利用两个模型，获得词语之间相似度、与某个词最想似的任意个词、与某篇文章最相似的任意篇文章、可以给出在模型中某个词或某篇文章的矢量表示。
## makecall.py:
（1）调用loadfromdb.py，整理文章入dbfiles

（2）调用clean_sentences.py，获得matchlist

（3）根据文章创建word2vec和doc2vec模型
（4）利用两个模型，获得词语之间相似度、与某个词最想似的任意个词、与某篇文章最相似的任意篇文章、可以给出在模型中某个词或某篇文章的矢量表示。

（4）有一些尝试性的helper functions，留在makecall.py中，但最后不需要调用。
