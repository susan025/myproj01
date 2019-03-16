if __name__ == '__main__':
    #编写Python程序判断字符串是否重复。
    #创建数据源
    mstr = "goodgoodstudy,daydayup"
    nstr = "yes"


    #将字符串加入set集合去重
    mset = set(mstr)
    print(mset)
    #判断数据源的长度是否大于set集合的长度
    if len(mstr) > len(mset):
        print("有重复字符")
    else :
        print("无重复字符")


    #编写Python程序打印输出字符串中重复的所有字符
    #创建列表，将字符串加入列表
    mlist = list(mstr)
    # 循环未去重的列表
    for i in list(mset):
        # 创建计数变量count
        count = 0
        #循环已去重的集合
        for j in mlist:
            #如果去重的集合中的元素与未去重的元素相等，计数加1
            if i == j:
                count += 1
        if count >= 2:
            # 打印结果
            print(i, end=" ")

