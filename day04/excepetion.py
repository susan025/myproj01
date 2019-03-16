if __name__ == '__main__':
    #异常
    try:
        print(5/0)
    except ZeroDivisionError as e:
        print("ZeroDivisionError")
        print(e)

    print("good")

    print("输入两个数，计算除法")
    print("输入q退出")

    while True:
        print("\t")
        fnum = input("First number:")
        if fnum == "q":
            break
        snum = input("Second number:")
        if snum == "q":
            break

        try:
            res = int(fnum)/int(snum)
        except ZeroDivisionError as e:
            print("division error")
        else:
            print("result = {0}".format(res))
        finally:
            print("处理收尾")