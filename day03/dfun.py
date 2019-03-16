
#传参函数
def regUser(name,pwd):
    print("name = {0}".format(name))
    print("pwd = {0}".format(pwd))

#参数默认值
def regLser(name,pwd="000"):
    print("name = {0}".format(name))
    print("pwd = {0}".format(pwd))

def regYser(name,pwd,nakename= ""):
    print("name = {0}".format(name))
    print("pwd = {0}".format(pwd))

def regOer(name,pwd,nakeName=" "):
    if nakeName:
        user = {"name":name,"pwd":pwd,"nakeName":nakeName}
    else:
        user = {"name":name,"pwd":pwd}
    return user

def getUserName(names):
    for n in names:
        print(n)

def getLserName(names):
    names.append("good")

#传递任意数量的实参
def mulPara(*params):
    print(type(params))
    for p in params:
        print(p)

#传递任意数量的实参
def mullPara(**params):
    print(type(params))
    for p in params.items():
        print(p)
if __name__ == '__main__':
    regUser(pwd="1234",name="gao")

    regLser(name="gao")

    regYser(pwd="123",name="gao")
    regYser(pwd="456",name="gao",nakename="shsan")

    u = regOer("good","4321",nakeName="gg")
    print(u)

    names = ["good","luck","to","me"]
    getUserName(names)

    getLserName(names)
    getLserName(names[:])
    print(names)

    mulPara("good","luck","to","me")

    mullPara(a="good",v="vv")