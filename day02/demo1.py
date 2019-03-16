if __name__ == '__main__':
    #两种创建列表的方式
    mlist = list()
    nlist = []
    print(type(mlist))
    print(type(nlist))

    #在列表中添加元素
    #使用append在列表尾添加数据
    mlist.append("校长")
    mlist.append("教导主任")
    mlist.append("辅导员")
    mlist.append("讲师")
    print(mlist)

    #使用insert在列表指定位置添加数据
    mlist.insert(0,"院长")
    print(mlist)

    #从列表中删除元素
    mlist.remove("院长")
    print(mlist)

    #使用pop从列表删除数据
    mlist.pop()
    print(mlist)

    val = mlist.pop()
    print("mlist.pop = {popval}".format(popval = val))
    print(mlist)

    #清除列表中的元素，保留列表本身
    mlist.clear()
    print(mlist)

    #删除整个列表
    del mlist

