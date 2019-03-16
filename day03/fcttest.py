import day03.functiontest
if __name__ == '__main__':
    #调用九九乘法表的方法
    n = int(input("请输入九九乘法表行数："))
    day03.functiontest.mullist(n)

    #调用等腰三角形的方法
    m = int(input("请输入等腰三角形的行数："))
    day03.functiontest.triangle(m)

    #调用菱形
    q = int(input("请输入菱形行数："))
    day03.functiontest.diamond(q)

    #调用数字正方形方法
    num = int(input("请输入数字范围："))
    day03.functiontest.square(num)