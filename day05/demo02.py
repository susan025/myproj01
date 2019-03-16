if __name__ == '__main__':
    # 2.创建一个列表，存储公司10个名单，对这些名单进行排序，要求按姓名的字符多少来排。（30分
    mlist = ["john","susan","backham","roy","乔","William","karry"]
    # for i in range(4):
    #     mlist.append(input("请输入名字："))
    print(mlist)
    nlist = [len(i) for i in mlist]
    print(nlist)
    glist = []
    a = 0
    i=0
    while i < len(nlist) :
        if nlist[i] >= a :
            a = nlist[i]
            glist.insert(0,mlist[i])
        else :
            k=0
            b = len(glist)
            while k < b :
                if nlist[i] >=len(glist[k]) :
                    glist.insert(k,mlist[i])
                    break
                if k == b-1 :
                    glist.append(mlist[i])
                k+=1
        i+=1
    print(glist)