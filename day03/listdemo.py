if __name__ == '__main__':
    #把一个list中所有的字符串变成小写
    llist = ['Hello', 'World', 'IBM', 'Apple']
    mlist = [i.lower() for i in llist ]
    print(mlist)

    #如果在list中既包含字符串，又包含其它类型数据，如何修改1中的生成式实现把一个list中所有的字符串变成小写
    qlist = ['Hello', 2, 'World', 3.5, 'IBM', 'Apple']
    wlist = [m.lower() for m in qlist if isinstance(m,str) for n in qlist if isinstance(n,int)]
    print(wlist)