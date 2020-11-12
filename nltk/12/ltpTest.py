from ltp import LTP

ltp = LTP()
sents = ltp.sent_split(["他叫汤姆去拿外衣。", "汤姆生病了。他去了医院。"])

for sent in sents:
    #分词
    seg, hidden = ltp.seg(list(sent))
    print(seg)
    #词性标注
    print(ltp.pos(hidden))
    #命名实体识别
    ner = ltp.ner(hidden)
    print(ner)
    if(len(ner[0]) != 0):
        tag, start, end = ner[0][0]
        print(tag, ":", "".join(seg[0][start:end + 1]))
    #语意角色标注
    srl = ltp.srl(hidden)
    print(srl)
    #依存句法分析
    dep = ltp.dep(hidden)
    print(dep)
    #语意依存分析
    sdp = ltp.sdp(hidden, graph=False)
    print(sdp)
    #图
    sdp = ltp.sdp(hidden, graph=True)
    print(sdp)

