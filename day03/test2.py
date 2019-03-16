if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up"]

    #去除空格
    mlist = list()
    for i in klist:
        str = i.strip()
        mlist.append(str)
    print(mlist)
    #放入集合，去重
    mset = set(mlist)
    #1.编写Python程序判断字符串是否重复
    if len(mlist) > len(mset):
        print("有重复字符串")
    else:
        print("无重复字符串")

    #2.编写Python程序打印输出字符串中重复的所有字符
    print("重复的字符串为",end=":")
    for m in mset:
        v = mlist.count(m)
        if v >= 2:
            print(m,end=" ")

    #3.把下面的klist作为字典的键
    #同时作为字典的值
    mdict = dict()
    for n in mset:
        mdict[n] = n
    print("\n字典：",mdict)

    #4.#把下面的klist作为字典的键
    #并统计每个单词的词频
    ndict = dict()
    for a in mset:
        ndict[a] = mlist.count(a)
    print("词频为",ndict,end=":")