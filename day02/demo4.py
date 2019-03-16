if __name__ == '__main__':
    #创建空列表
    mlist = []
    print(type(mlist))

    #创建非空列表
    nlist = [1,2,3,4]
    print(type(nlist))

    #for循环遍历
    for i in nlist:
        print("nlist[{0}] = {1}".format(i.__index__(),i))

    #遍历
    for l in nlist:
        print(l)

    #改变列表中的数
    nlist[0] = 10
    for n in nlist:
        print(n)