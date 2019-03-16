if __name__ == '__main__':
    uname = "gaoshan"
    upassword = "haha"
    usex = "man"

    #默认print的使用方式
    print(uname,upassword,usex)
    #替换行尾的换行，输出不换行，用end实现
    print(uname,upassword,usex,end=" ")
    #参数之间去掉一个间隔符（空格），使用sep参数实现
    print(uname,upassword,usex,sep="-")

    #格式化输出
    mname = input("you name:")

    #使用了字符串的格式化输出功能
    #将format参数按照顺序填写到前面字符串的占位符位置
    print("good to you {0}".format(mname))

    print("you name is {name} and your age = {age}".format(name="gaoshan",age=18))


