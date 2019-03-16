if __name__ == '__main__':
    #复制列表
    mlist = [1,2,3,4]
    nlist = mlist[:]

    nlist[0] = 3

    print("nlist = {0}".format(nlist))
    print("mlist = {0}".format(mlist))

    #求列表长度
    print("len of mlist = ",len(mlist))
    #求列表最大值
    print("max of mlist = ",max(mlist))
    #求列表最小值
    print("min of mlist = ",min(mlist))

    #常用函数-count
    qlist = ["嘻嘻","嘿嘿","嘻嘻","嘻嘻","吼吼"]
    num = qlist.count("嘻嘻")
    print(num)

    #常用函数-extend
    qlist.extend(mlist)
    print("list.extend ->",qlist)

    #常用函数-添加删除
    mlist.append(33)
    print("list.append->",mlist)

    mlist.insert(0,44)
    print("list.insert->",mlist)

    v = mlist.pop(0)
    print("list.v->",v)
    print("list.pop->",mlist)

    mlist.remove(1)
    print("list.remove->",mlist)

    #先判断被删除的数值在列表中是否存在
    #再进行删除
    if 4 in mlist:
        mlist.remove(4)
    #使用try语句处理删除不存在数据产生的异常
    try:
        mlist.remove(5)
    except Exception as e:
        print("5 is not exist")
        print(e)
    finally:
        print("finally")

    #常用函数-copy
    tlist = mlist.copy()
    print("tlist id = ",id(tlist))
    print("mlist id = ",id(mlist))