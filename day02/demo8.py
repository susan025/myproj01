if __name__ == '__main__':
    #创建非空列表
    mlist = [1,2,3,4,5,6,7,8,9,0]
    #创建一个临时变量
    t = 2
    #是否包含操作
    print("in ->",t in mlist)
    print("not in ->",t not in mlist)

    #列表-遍历
    for m in mlist:
        print("mlist[{0}] = {1}".format(m.__index__(),m))

    #使用range初始化一个list
    nlist = [i for i in range(1,10)]
    print(nlist)

    #双层列表
    qlist = [[7,8,9],[4,5,6],[1,2,3]]
    for sublist in qlist:
        for j in sublist:
            print("qlist[{0}] = {0}".format(j,j.__index__()))

    #通过已有的列表创建一个新列表
    olist = [o for o in mlist]
    print("olist = ",olist)

    #查看id
    print("olist id ->",id(olist))
    print("mlist id ->", id(mlist))

    #列表中元素的偶数放到新的列表里
    olist = [o for o in mlist if o % 2 == 0]
    print("olist = ",olist)

