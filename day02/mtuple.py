if __name__ == '__main__':
    #创建一个元组
    mytuple = (1,2,3,4,5)
    #元组索引
    print("mytuple[{1}] = {0}".format(mytuple[0],0))
    #元组的遍历
    for i in mytuple:
        print("mytuple->",i)

    #元组的切片
    ntuple = mytuple[0:3:1]
    print("ntuple = ",ntuple)

    #传址
    qtuple = mytuple
    print("id of qtuple->",id(qtuple))
    print("id of mtuple->",id(mytuple))

    #传值
    qtuple += mytuple
    print("id of += qtuple->",id(qtuple))