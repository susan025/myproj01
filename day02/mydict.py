if __name__ == '__main__':
    #创建一个非空字典
    mdict = {"name":"good","age":18}

    #创建一个空字典
    ndict = dict()

    #查看数据类型
    print(type(mdict))
    print(type(ndict))

    #创建一个非空字典，key使用元组
    qdict = {"name":"good","age":18,("addr"):"gen"}
    print(qdict)

    #创建非空字典1
    wdict = {"one":1,"two":2,"three":3}
    print(wdict)

    #创建非空字典2
    edict = ({"one":1,"two":2,"three":3})
    print(edict)

    #创建非空字典3
    rdict = dict(one=1,two=2,three=3)
    print(rdict)

    #创建非空字典4
    tdict = dict([("one",1),("two",2),("three",3)])
    print(tdict)

    #修改字典
    mdict["age"] = 20
    print(mdict)

    #将字典转换成字符串
    msdict = str(mdict)
    print(type(msdict))
    print(msdict)

    #求字典长度
    dictlen = len(mdict)
    print(dictlen)

    #获取数据类型
    mtype = type(mdict)
    print(mtype)

    #访问数据
    m1 = mdict["name"]
    print(m1)

    #删除数据
    del wdict["one"]
    print(wdict)

    #遍历
    for k in rdict:
        print("dict[{0}] = {1}".format(k,rdict[k]))

    #根据键来取值
    for u in rdict.keys():
        print("dect[{0}] = {1}".format(u,rdict[u]))

    #直接使用字典方法values
    for v in rdict.values():
        print("rdict[{1}] = {0}".format(v.__index__(),v))

    #同时取出键和值
    for g,h in rdict.items():
        print("rdict[{1}] = {0}".format(g,h))

    #字典生成式
    ydict = {i:o for i,o in rdict.items()}
    print("ydict = ",ydict)
    # 字典生成式 - 偶数
    udict = {i:o for i,o in rdict.items()}
    print("udict = ",udict)

    #字典长度
    mlen = len(rdict)
    print(mlen)
    #字典最大值
    maxdict = max(rdict)
    print(maxdict)
    #字典最小值
    mindict = min(rdict)
    print(mindict)

    #方法items
    di = rdict.items()
    print(type(di))
    print(di)
    #方法keys
    nk = rdict.keys()
    print(type(nk))
    print(nk)
    #方法values
    nv = rdict.values()
    print(type(nv))
    print(nv)

    #删除字典中的数据
    del mdict["age"]
    print(mdict)

    #删除字典
    del mdict
    print(mdict)