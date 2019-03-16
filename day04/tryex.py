#抛出异常
def mfun(v):
    if v == 0:
        raise Exception("good")

if __name__ == '__main__':
    #异常处理
    #打开一个不存在的文件
    try:
        mfile = open("good.text","r")
        mfile.close()
    except Exception as e:
        print(e)
    else:
        print("excetion else")
    finally:
        print("finally")

    try:
        mfun(0)
    except Exception as e:
        print("excetp->{0}".format(e))
        pass

    print("good")