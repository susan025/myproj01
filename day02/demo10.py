import random
if __name__ == '__main__':
    #循环十次产生10个随机数，随机数的选取范围在0-100之间
    mlist = [random.randint(0,100) for i in range(0,10)]
    print(mlist)

    nstr = range(1,3)
    print(nstr)
