if __name__ == '__main__':
    #创建非空列表
    mlist = [1,2,3,4,5,6,7,8,9,0]
    #查看id
    print("mlist-id:",id(mlist))
    #删除mlist中的第一元素
    del mlist[0]
    print(mlist)

    #再次查看id
    print("mlist-id:",id(mlist))