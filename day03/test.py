if __name__ == '__main__':
    #
    klist = ["good ","good ","study",
    " good ","good","study ",
    "good "," good"," study",
    " good ","good"," study ",
    "good ","good ","study",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
" day ","day"," up"]

    kset = set()
    vset = set()
    #去除空格
    for i in klist:
        str = i.strip()
        kset.add(str)
        vset.add(str)

    print(kset)
    print(vset)

    #创建字典
    mdict = dict()
    for m in kset:
        mdict[m] = m
    print(mdict)