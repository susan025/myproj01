#九九乘法表
if __name__ == '__main__':
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in num:
        for j in num:
            a = i*j
            print(j,end="*")
            print(i,end="=")
            print(str(a).rjust(2),end=" ")
            # print(j,i,sep="*",end="=")
            # print(a,end=" ")
            if i == j:
                print()
                break

#0-119 正方块
    num = 0
    for i in range(0,120):
        if num%10 == 0:
            print()
        print(str(i).rjust(3),end=" ")
        num += 1
