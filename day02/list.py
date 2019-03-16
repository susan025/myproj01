if __name__ == '__main__':
    mlist = list()
    nlist = []
    print(type(mlist))
    print(type(nlist))

    mlist.append("老师")
    mlist.append("老师1")
    mlist.append("老师2")
    mlist.append("老师3")
    print(mlist)

    # mlist.insert(0,"辅导员")
    # print(mlist)
    #
    # mlist.insert(4,"院长")
    # print(mlist)

    mlist.pop()
    print(mlist)

    del mlist[0]
    print(mlist)

    # del mlist

