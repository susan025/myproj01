import random
# if __name__ == '__main__':
#     print("姓名：高山")
#     print("性别：女")
#     print("年龄：18")
#
#     print(16**1/2)
a = int(input("输入一个整数："))
v = random.randint(0,a)
print(int(v))

if v > a:
    print("最大数为：",v)
elif v < a:
    print("最大数为：",a)