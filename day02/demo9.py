if __name__ == '__main__':
    #创建一个非空列表
    mlist = [1,2,3,4]

    nlist = [100,200,300,400]

    qlist = [m+n for m in mlist for n in nlist]
    print("no if ->",qlist)

    wlist = [a+b for a in mlist if a % 2 == 0 for b in nlist]
    print("no if ->",wlist)

    #创建源数据
    elist = [['a','b'],['e','f'],['g','h']]

    #遍历创建一个新的列表
    rlist = [[x,y] for x,y in elist]
    print(rlist)