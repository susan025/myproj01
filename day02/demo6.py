if __name__ == '__main__':
    #列表id 的使用
    #创建一个非空列表
    mlist = [1,2,3,4,5,6,7,8,9,0]

    #分片
    nlist = mlist[-2:-4:-1]

    #打印id值
    print("mlist-id：",id(mlist))
    print("nlist-id：", id(nlist))

    #将Mlist赋值 给slist
    slist = mlist
    #输出id值
    print("mlist-id:",id(mlist))
    print("slist-id:", id(slist))