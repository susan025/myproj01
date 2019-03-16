import day04.question1.p1 as p
if __name__ == '__main__':
    mdict = {
        1:"[1]输入用户姓名及性别，然后给出下列的提示：XX先生你好 或 XX女士你好",
        2:"[2]随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3:"[3]注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）",
        4:"[4]从键盘输入一行字符串，判断是否是回文数"
    }
    mfunction = {
        1:p.checkSex,
        2:p.bing,
        3:p.email,
        4:p.hui
    }

    for c in mdict.values():
        print(c)

    while True:
        print()
        n = input("请选择功能编号：")

        print(mdict[int(n)])

        mfunction[int(n)]()