if __name__ == '__main__':
    #定义字典
    mdict = {}
    #定义key键list
    klist = ["name","age","sex"]
    vlist = ["susan","18","men"]
    for k in klist:
        mdict[k] = vlist[klist.index(k)]
    print(mdict)


    list1 = [1, 2, 3]
    if (len(list1) != len(set(list1))):
        print("重复")
    else:
        print("不重复")