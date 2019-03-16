if __name__ == '__main__':
    #find
    mstr = "good good study, day day up"
    mindex = mstr.find("good")
    print(mindex)

    nindex = mstr.find("good",1)
    print(nindex)

    sindex = mstr.find("good",1,10)
    print(sindex)

    #index
    aindex = mstr.index("good")
    print(aindex)

    bindex = mstr.index("good",1)
    print(bindex)

    cindex = mstr.index("good",1,10)
    print(cindex)

    