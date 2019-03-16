#编写Python程序判断字符串是否重复。
if __name__ == '__main__':
    n = str(input("请输入一个字符串："))
    mset = set(n)
    print(mset)
    if len(n) > len(mset):
        print("有字符重复")
    else:
        print("无字符重复")

#编写Python程序打印输出字符串中重复的所有字符。
    nlist = list(n)
    for i in list(mset):
        count = 0
        for j in nlist:
            if i == j:
                count += 1
        if count >= 2 :
            print(i,end=" ")


