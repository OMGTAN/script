# coding:utf-8
 
from ltp import LTP

ltp = LTP()
sents = ltp.sent_split(["他叫汤姆去拿外衣。", "汤姆生病了。他去了医院。"])

for sent in sents:
    l1 = [sent]
    # l1.append(sent)
    #分词
    seg, hidden = ltp.seg(l1)
    print(seg)
    #词性标注
    print(ltp.pos(hidden))
    #命名实体识别
    ner = ltp.ner(hidden)
    print("命名实体识别", ner)
    if (len(ner[0]) != 0):
        tag, start, end = ner[0][0]
        print(tag, ":", "".join(seg[0][start:end + 1]))
    #语义角色标注
    srl = ltp.srl(hidden)
    print("语义角色标注", srl)
    #依存句法分析
    dep = ltp.dep(hidden)
    print("依存句法分析", dep)
    #语义依存分析
    sdp = ltp.sdp(hidden, graph=False)
    print("语义依存分析", sdp)
    #图
    sdp = ltp.sdp(hidden, graph=True)
    print("语义依存分析 图", sdp)
