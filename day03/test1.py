if __name__ == '__main__':
    klist = ["good ", "good ", "study",
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
    mset = set(mlist)
    print(mset)

    #编写Python程序判断字符串是否重复
    if len(mlist) > len(mset):
        print("有重复字符串")
    else :
        print("无重复字符串")

    #编写Python程序打印输出字符串中重复的所有字符
    print("重复的字符串为",end=":")
    for m in mset:
        v = mlist.count(m)
        if v >= 2:
            print(m,end=" ")

    #统计词频
    #创建字典
    print("\n 重复的次数为",end=":")
    mdict = dict()
    for d in mset:
        mdict[d] = mlist.count(d)
    print(mdict)

    #匹配键值
    ndict = dict()
    for n in mset:
        ndict[n] = n
    print(ndict)