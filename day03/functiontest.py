
#九九乘法表函数
def mullist(n):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in num:
        for j in num:
            if i <= n:
                a = i * j
                print(j, i, sep="*", end="=")
                print(a, end=" ")
                if i == j:
                    print()
                    break

#等腰三角形函数
def triangle(n):
    nstr = range(1,2*n)
    for i in nstr[0:n]:
        for j in nstr[n-i:0:-1]:
            print(" ",end=" ")
        for j in nstr[0:2*i-1]:
            print("*",end=" ")
        print(" ")

#菱形函数
def diamond(n):
    nstr = range(1, 2 * n)
    for i in nstr[0:n]:
        for j in nstr[n - i:0:-1]:
            print(" ", end=" ")
        for j in nstr[0:2 * i - 1]:
            print("*", end=" ")
        print(" ")
    for i in nstr[0:n-1]:
        for j in nstr[0:i]:
            print(" ",end=" ")
        for j in nstr[2*(n-i)-1:0:-1]:
            print("*",end=" ")
        print(" ")
#正方形数字
def square(n):
    num = 0
    for i in range(0, n+1):
        if num % 10 == 0 and num != 0:
            print()
        print(str(i).rjust(3), end=" ")
        num += 1