import random

def checkSex():
    #输入用户姓名及性别，然后给出下列的提示：（20分）XX先生你好 或 XX女士你好
    name = input("请输入你的姓名：")
    sex = input("请输入你的性别：")
    #创建字典
    sexdict = {
        "男":True,"man":True,"male":True,"Mrs":True,"boy":True,
        "女":False,"woman":False,"female":False,"Miss":False,"girl":False
    }
    if sexdict[sex]:
        print("{0}先生你好".format(name))
    else :
        print("{0}女士你好".format(name))

def bing():
    #随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集
    mlist = [random.randint(0,10) for i in range(0,10)]
    nlist = [random.randint(0,10) for i in range(0,15)]
    mset = set(mlist)
    nset = set(nlist)
    qset = mset | nset
    print("两个列表的并集为:",qset)

def email():
    #注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息
    email = str(input("请输入邮箱："))
    if "@" not in email:
        print("请输入正确的格式，如fs123@qq.com")
    else:
        print("邮箱格式正确，您的邮箱为：",email)

def hui():
    #从键盘输入一行字符串，判断是否是回文数
    nstr = str(input("请输入一个整数："))
    mlist = []
    for i in nstr:
        mlist.append(i)
    nlist = mlist.copy()
    nlist.reverse()
    if mlist == nlist:
        print("{0}是回文数".format(nstr))
    else:
        print("{0}不是回文数".format(nstr))
