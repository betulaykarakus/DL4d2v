# DL4d2v

# 一、所有文件的作用
## （一） text files
### userdict：
分词字典。
### puntuation.txt
分句和分词所需标点和特殊符号。
### stereowords.txt:
每一行以“样词 类别”格式的每一类词语样例，由w2v&d2v模型提供的词语相似度生成。在makecall.py调用创建模型的d2vmodel.py和w2vmodel.py之后，可以使用w2vmodel.py和d2vmodel.py中利用已创建模型得到相似度的方法来生成这个txt文件。
### topicslist.txt：
认为需要的话题列表分行文件。
## （二） python files
### loadfromdb.py:
（1）从数据库取得文章

（2）把文章标题改成有顺序的编号，存入文件夹dbfiles

（3）获得每篇文章的原标题和现有编号对应表，记录在matchlist.txt中。

### clean_sentences.py:
（1）获得matchlist

（2）所有dbfiles中的文章，分句，并且分词之后，以同样名称存入文件夹segmented中。

### givewordstype.py:
（1）把stereowords.txt中样词和对应类别存入字典samples

（2）从topicslist.txt得到话题，即文章所对应的方向类型。

（3）有选择的从segmented文件夹中选取一部分文件到segmented2文件夹，对其中的文件生成雷达图。（这一步可以将所有segmented2直接改成segmented）

（4）根据每篇文章高频词所在类别决定每篇文章在每个方向上的比例分布，得到可以画雷达图的数据。
### w2vmodel.py和d2vmodel.py：
（1）创建两种模型

（2）SAVE & LOAD 两种模型

（3）利用两个模型，获得词语之间相似度、与某个词最想似的任意个词、与某篇文章最相似的任意篇文章、可以给出在模型中某个词或某篇文章的矢量表示。
### makecall.py:
（1）调用loadfromdb.py，整理文章入dbfiles

（2）调用clean_sentences.py，获得matchlist

（3）根据文章创建word2vec和doc2vec模型
（4）利用两个模型，获得词语之间相似度、与某个词最想似的任意个词、与某篇文章最相似的任意篇文章、可以给出在模型中某个词或某篇文章的矢量表示。

（4）有一些尝试性的helper functions，留在makecall.py中，但最后不需要调用。
# 二、用法示例 DEMOS
### Demo 0: 给文章分句及分词
+ 例 文章如下：
>生活中儿童糖尿病发病前征兆不怎么明显，需要家长提高警惕。小儿饭量大增，这个特点很容易被忽略。家长多认为是孩子生长发育中的正常情况，但应注意是否出现其他糖尿病征兆。与此同时小儿突然消瘦，孩子正处于生长发育期，体重应该连续稳定上升，但突然出现体重下降情况，家长要警惕儿童糖尿病的发生。

+ 将以上文章作为 "a_1.txt" 存在于文件夹 dbfiles 中。
+ 直接用clean_sentences.py中的分句函数fenju()，即在 clean_sentences.py 结尾加上：<br/>
>    fenju()<br/>
+ 然后运行：<br/>
> python clean_sentences.py
+ 已经分好句也分好词的结果在文件夹segmented中作为a_1.txt显示：
>生活 儿童 糖尿病 发病 前 征兆 不怎么 明显 需要 家长 提高警惕 <br/>小儿 饭 量大增 这个 特点 很 容易 被 忽略<br/>
家长 多 认为 是 孩子 生长发育 正常 情况 但应 注意 是否 出现 其他 糖尿病 征兆<br/>
与此同时 小儿 突然 消瘦 孩子 正 处于 生长 发育期 体重 应该 连续 稳定上升 但 突然 出现 体重 下降 情况 家长 要 警惕 儿童 糖尿病 发生<br/>
+ **参考样例：demo-0.py**，五篇样例语料库的文章在文件夹textsfordemos里面。分句和分词的五篇文章结果在segmentedfordemos文件夹里。


### Demo 1: 创建保存及调出已保存模型
+ demo1.1: 创建并保存word2vec模型:
  + 在loadfromdb.py中修改相关数据库名称等信息，或者直接把语料库排序后放入dbfiles(省略makecall.py中).
  + >      python makecall.py
  + 文件夹models中将会出现模型w2v.model
  + **参考样例：demo-1-1.py**，建议在运行demo-0.py之后进行，所用文章来自已经分好词的segmentedfordemos文件夹，model结果会在"models"文件夹的"textw2v.model"文件中
+ demo1.2: 创建并保存document2vec模型:
  + 在loadfromdb.py中修改相关数据库名称等信息，或者直接把语料库排序后放入dbfiles(省略makecall.py中).
  + 用以下代码替换makecall.py中的makemodels函数：
  > os.system("mkdir models") <br/>
  > d2vmodel.make_d2v()
  + >      python makecall.py
  + 文件夹models中将会出现模型d2v.model
  + **参考样例：demo-1-2.py**，建议在运行demo-0.py之后进行，所用文章来自已经分好词的segmentedfordemos文件夹，model结果会在"models"文件夹的"textd2v.model"文件中
+ demo1.3: 调出已保存的word2vec模型:
  + 例如模型已经被保存在文件夹models中，称为w2v.model
  + 在 w2vmodel.py 结尾加上：
  > load_w2v()
  + >      python w2vmodel.py <br/>

  或在要使用模型前在任意文件里先load_w2v()即可使用。
  + **参考样例：demo-1-3.py**，建议在运行demo-1-1.py之后进行。
+ demo1.4: 调出已保存的document2vec模型:
  + 例如模型已经被保存在文件夹models中，称为d2v.model
  + 在 d2vmodel.py 结尾加上：
  > load_d2v()
  + >      python d2vmodel.py

  或在要使用模型前在任意文件里先load_d2v()即可使用。
  + **参考样例：demo-1-4.py**，建议在运行demo-1-2.py之后进行。

### Demo 2: 从文章提取特征词及获得特定词的矢量表示
根据以上Demo 1,将文章作为唯一defiles文件夹中的文件，并创建出word2vec模型后，该模型可以直接阅读，每行第一个词语即为文章特征词。<br/>
可以分别提取多篇文章中每一篇的特征词，也可以将多篇文章视为一个语料库提取共同的特征词。<br/>
要获得特定词的矢量表示，
> model = load_w2v()<br/>
> print model[u"特定词"]

+ **参考样例：demo-2.py**，建议在运行demo-0.py之后进行，所用文章来自已经分好词的segmentedfordemos文件夹。

### Demo 3: 从文章获取词语之间相似度大小/亲近关系
根据以上Demo 1，创建出word2vec模型，在主程序结尾调用w2vmodel.py中的sim_btw_ws(）函数。<br/>
  例如可以在 w2vmodel.py 结尾加上：  
> model = load_w2v()<br/>

  比较词语w1和w2之间的相似度：<br/>
> print sim_btw_ws(w1, w2, model)

+ **参考样例：demo-3.py**，建议在运行demo-0.py之后进行，所用文章来自已经分好词的segmentedfordemos文件夹。

### Demo 4: 从文章中得到与某一个词最相似的N个词
根据以上Demo 1，创建出word2vec模型，在主程序结尾调用w2vmodel.py中的topn_sim_word(）函数。<br/>
  例如可以在 w2vmodel.py 结尾加上：  
> model = load_w2v()<br/>

得到与词w1最相似的N个词：<br/>
> print topn_sim_word(w1, topn=N, model)

+ **参考样例：demo-4.py**，建议在运行demo-0.py之后进行，所用文章来自已经分好词的segmentedfordemos文件夹。

### Demo 5: 从多篇文章中获取与某一篇文章最相似的N篇文章
根据以上Demo 1，创建出document2vec模型，在主程序结尾调用d2vmodel.py中的find_sim_docs(）函数。<br/>
  例如可以在 d2vmodel.py 结尾加上：  
> model = load_d2v()<br/>

要得到与id=9最相似的N篇文章：<br/>
> find_sim_docs(model, 9, N)

+ **参考样例：demo-5.py**，建议在运行demo-1-4.py之后运行，用textsfordemos文件夹中的五篇文章。如果要对document2vec有更多运用，需要在创建模型是规定每一篇文章的ID顺序。

### Demo 6: 从多篇文章形成的D2V模型中获取某个ID对应文章的矢量表示
根据以上Demo 1，创建出document2vec模型，在主程序结尾调用d2vmodel.py中的output_doc_vec(）函数。<br/>
  例如可以在 d2vmodel.py 结尾加上：  
> model = load_d2v()<br/>

要得到与id=9文章的矢量表示：<br/>
> output_doc_vec(model, 9)

+ **参考样例：demo-6.py**，建议在运行demo-1-4.py之后运行，用textsfordemos文件夹中的五篇文章。如果要对document2vec有更多运用，需要在创建模型是规定每一篇文章的ID顺序。
