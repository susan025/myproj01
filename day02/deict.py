if __name__ == '__main__':
    ndict = {"one":1,"two":2,"three":3}
    #调用字典方法get
    ng = ndict.get("two")
    print("type of get =",type(ng))
    print(ng)
    #调用字典方法clear
    ndict.clear()
    print(ndict)

    #定义一个字典
    mlanguage = {"j":"java","c":"c","p":"python"}
    for l in sorted(mlanguage.keys()):
        print(mlanguage[l])

    for v in sorted(mlanguage.values()):
        print(v)