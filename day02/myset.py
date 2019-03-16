if __name__ == '__main__':
    #创建一个空的集合
    mset = set()

    #打印mset的类型
    print("mset type = ",type(mset))

    #创建一个非空集合，另一种方式
    nset = {1,2}
    #打印nset的类型
    print("nset type = ",type(nset))

    qset = {1,2,3,3,4,4,5}
    wset = set(qset)
    print(wset)

    eset = set("good luck")
    print(eset)

    #成员检测
    if 4 in eset:
        print("4 exist in eset")
    if 10 not in eset:
        print("10 not in eset")

    rset = {1,2,"good","luck",5}
    for n in rset:
        print("nset = {0}".format(n))

    tset = {(1,2,3),(4,5,6),(7,8,9)}
    for n,p,q in tset:
        print("tset = ",n,p,q)

    sset = {i for i in qset}
    print("sset = ",sset)

    sset = {i for i in qset if i % 2 == 0}
    print("sset = ",sset)

    #创建两个set
    aset = {1,2,3,3,4,4,5}
    bset = {7,9,8,3}
    #求并集
    gset = aset|bset
    print(gset)
    #求交集
    gset = aset&bset
    print(gset)
    #求差集
    gset = aset - bset
    print(gset)
    #去并集中的交集
    gset = aset ^ bset
    print(gset)

    #求长度1
    l = aset.__len__()
    print(l)
    #求长度2
    l = len(aset)
    print(l)
    #求集合中的最大值
    mmax = max(aset)
    print(mmax)
    mmin = min(aset)
    print(mmin)

    #添加新的数据
    bset.add(10)
    print(bset)
    bset.update({99,88,77})
    print(bset)

    #复制
    pset = aset.copy()
    print("aset.copy = ",pset)

    print(id(aset),id(pset),sep="\r\n")

    #对集合清空
    pset.clear()
    print("set.clear = ",pset)

    len = aset.__len__()
    i = 0
    while True:
        if i >= len:
            break
        v = aset.pop()
        print(v)
        i+=1

    #移除元素
    qset.remove(3)
    print(qset)

    #移除不报错
    qset.discard(100)
    print(qset)

    fset = {1,2,3,3,4,4,5}
    hset = {1,2}
    #求交集
    vset = fset.intersection(hset)
    print(vset)
    #求交集
    vset = fset.difference(hset)
    print(vset)
    #并集
    vset = fset.union(hset)
    print(vset)
    #判断
    vis = fset.issubset(hset)
    print(vis)
    nis = fset.issuperset(hset)
    print(nis)

    #数学运算
    yset = fset - hset
    print(yset)

    #冰冻集合
    nfs = frozenset(fset)
    print(nfs)