# coding:utf-8
import sys
import importlib
importlib.reload(sys)
# coding:utf-8

import pynlpir

pynlpir.open()
s = '聊天机器人到底该怎么做呢？'
segments = pynlpir.segment(s)
for segment in segments:
    print (segment[0],  segment[1])

key_words = pynlpir.get_key_words(s, weighted=True)
for key_word in key_words:
    print (key_word[0], key_word[1])

pynlpir.close()