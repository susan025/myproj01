import random
if __name__ == '__main__':
    #随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中
    print("序列为",end=":")
    mlist = list()
    for i in range(0,5):
        m = [random.randint(0,10)]
        mlist.append(m)
    print(mlist)
    print("整数为",end=":")
    n = [random.randint(0,10)]
    print(n)
    if mlist.index(n):
        print("这个整数在序列中")
    else:
        print("这个整数不在序列中")