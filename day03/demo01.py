if __name__ == '__main__':
    #通过构造传参创建列表
    mlist = list(range(1,11))

    print("mlist = {mlistkey}".format(mlistkey=mlist))

    #生成[1*1,2*2,3*3,...,10*10]
    nlist = list()
    for i in range(1,11):
        nlist.append(i**2)
    print(nlist)

    #利用列表生成式生成
    slist = [i**2 for i in range(1,11)]
    print("slist = {slistkey}".format(slistkey=slist))

    #条件判断
    hlist = list()
    for i in range(1,11):
        if i % 2 == 0:
            hlist.append(i)
    print(hlist)

    #列表生成式—条件判断
    glist = [i for i in range(1,11) if i % 2 == 0]
    print(glist)