# 对一字符串进行翻转操作
def myStr():
    str = "nameisgod"
    mlist = []
    for i in str:
        mlist.append(i)
    print(mlist)
    mlist.reverse()
    print(mlist)
    mstr = ""
    for j in mlist:
        mstr += j
    print(mstr)

    # 创建一个列表，存储公司10个名单，对这些名单进行排序，要求按姓名的字符多少来排
def compName():
    clist = ["john","susan","backham","roy","乔","William","karry"]
    llist = []
    mdict = dict()
    for i in clist:
        v = len(i)
        llist.append(v)
    print(llist)
    for j in clist:
        mdict[j] = llist[clist.index(j)]
    print(mdict)
    mdict.values()

    for n in mdict.keys():
        pass

#输入用户名密码进行注册，要求用户名允许数字字母6-16位，密码6-16位，不允许出现*#!
def regist():
    username = str(input("请输入用户名："))
    password = str(input("请输入密码："))
    namebool1 = len(username) >= 6 and len(username)<=16
    namebool2 = "*" not in username and "#" not in username and "!" not in username
    pwdbool1 = len(password) >= 6 and len(password)<=16
    pwdbool2 = "*" not in password and "#" not in password and "!" not in password
    if namebool1:
        if namebool2:
            if pwdbool1:
                if pwdbool2:
                    print("注册成功！")
                else:
                    print("密码中不能含有*#！")
            else:
                print("密码必须6-16位")
        else:
            print("用户名中不能含有*#！")
    else:
        print("用户名必须6-16位")

def sstr():
    #输入一个字符串为社会主义核心价值观的全拼，每个词用空格进行分隔，将这个字符串，转成列表，遍历输出
    str = "she hui zhu yi he xin jia zhi guan"
    mlist = list(str.split(" "))
    print(mlist)


if __name__ == '__main__':

    myStr()
    compName()
    regist()
    sstr()



