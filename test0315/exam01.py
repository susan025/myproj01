if __name__ == '__main__':
    #输入两个人的生日，比较两个人年龄大小
    birth1 = str(input("请输入生日：（格式如：19990104）:"))
    year1 = int(birth1[0:4])
    # print(year1)
    birth2 = str(input("请输入第二位的生日：（格式如：19990104）："))
    year2 = int(birth2[0:4])
    # print(year2)
    if year1 < year2:
        print("第一位比第二位年龄大")
    else:
        print("第二位比第一位年龄大")