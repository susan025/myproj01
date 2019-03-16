#九九乘法表
if __name__ == '__main__':
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = int(input("请输入行数："))
    for i in num:
        for j in num:
            if i <= n:
                a = i*j
                print(j,i,sep="*",end="=")
                print(a,end=" ")
                if i == j:
                    print()
                    break




