
# if __name__ == '__main__':
#     while True:
#         a = input("请输入")
#         if a == "q":
#             break
#         elif a == "c":
#             print("this is c")
#         else:
#             print(a)
#     print("你好") #输出

if __name__ == '__main__':
# #字符串切片
#     mstr = "u can u up, u can u go"
#     print(mstr[1:10:-1])
#
# #字符串大小写转换
#

#九九乘法表
    num = [1,2,3,4,5,6,7,8,9]
    print("请输入一个整数")
    ii = input()

    for i in num:
        for j in num:
            a=i*j
            print(i, j, sep="*", end="=")
            print(a,end=" ")
            if i == j:
                print()
                break


