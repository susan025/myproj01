if __name__ == '__main__':
    mstr = "good good study, day day up"

    #count
    mcount = mstr.count("good")
    print(mcount)

    ncount = mstr.count("good",1)
    print(ncount)

    scount = mstr.count("good",1,10)
    print(scount)