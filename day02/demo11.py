if __name__ == '__main__':
    #切片创建
    mlist = [1,2,3,4]
    nlist = mlist[0:2]

    for i in nlist:
        print("nlist[{0}] = {1}".format(i.__index__(),i))

    mmlist = [1,2,3,4,5,6,7,8,9,0]
    nnlist = mmlist[0:6:2]

    for j in nnlist:
        print("nnlist[{0}] = {1}".format(j.__index__(),j))

    #反向切片
    bblist = mmlist[-4:-2]
    for n in bblist:
        print("反向切片--bblist[{0}] = {1}".format(n.__index__(),n))

    sslist = mmlist[-2:-4:-1]
    for l in sslist:
        print("反向切片--sslist[{0}] = {1}".format(l.__index__(),l))
