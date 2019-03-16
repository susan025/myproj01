if __name__ == '__main__':

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
                if nlist[i] >len(glist[k]) :
                    glist.insert(k,mlist[i])
                elif k == len(glist[k])-1 :
                    glist.append(mlist[i])
                k+=1
        i+=1

    print(glist)