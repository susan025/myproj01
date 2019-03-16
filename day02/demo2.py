import random
if __name__ == '__main__':
    #组织列表 -- 排序
    #为列表做永久性排序
    num = [3,7,4,2]

    #打乱顺序
    random.shuffle(num)
    print(num)

    #对列表进行升序排列
    num.sort()
    print(num)

    #对列表进行降序排列
    num.sort(reverse=True)
    print(num)

    #对列表进行临时降序排序
    snum = sorted(num,reverse=True)
    print(snum)

    #反转列表元素的排列顺序
    num.reverse()
    print(num)