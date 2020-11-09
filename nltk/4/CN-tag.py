# coding:utf-8

import sys
import importlib
importlib.reload(sys)
# coding:utf-8

import nltk
for word in nltk.corpus.sinica_treebank.tagged_words():
    print (word[0], word[1])