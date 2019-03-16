if __name__ == '__main__':
    #把下面的klist作为字典的键
    #并统计每个单词的词频
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

    #创建set集合
    mset = set()
    #nlist集合
    nlist = list()
    #去除空格
    for i in klist:
        #取出每个字符串的空格
        str = i.strip()
        #将字符串加入list
        nlist.append(str)
        #将字符串加入set，去重
        mset.add(str)
    print(mset)
    print(nlist)

    # 编写Python程序判断字符串是否重复
    #比较长度
    if len(nlist) > len(mset):
        print("有重复字符串")
    else:
        print("无重复字符串")

    #编写Python程序打印输出字符串中重复的所有字符
    for b in mset:
        v = nlist.count(b)
        if v >= 2:
            print(b)

    #统计词频
    #创建字典
    mdict = dict()
    #循环去重的set集合
    for m in mset:
        #以set集合中的元素m为键，计数count为值，为字典中的键赋值
        mdict[m] = nlist.count(m)
    #输出
    print(mdict)


