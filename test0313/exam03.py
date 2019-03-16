import random
#猜大小游戏：输入一个整数，随机生成一个数字，比较这两个数字的大小，并输出比较结果（40分）
if __name__ == '__main__':
    n = int(input("输入一个100以内的整数："))
    #取1-100随机数
    v = random.randint(0,100)
    print("随机数为：",v)
    #比较大小
    if n > v:
        print("两数中最大数是输入的整数：",n)
    elif n < v:
        print("两数中最大数是随机数：",v)