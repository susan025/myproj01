if __name__ == '__main__':
        mfile=open(r"C:\Users\Administrator\Desktop\8e37104700b408123e23b592beef4f5b.png","rb")
        mbool=mfile.read()
        print(mbool)

        nfile=open(r"C:\Users\Administrator\Desktop\8e37104700b3e23b592beef4f5b.png","wb")
        nn=nfile.write(mbool)
        print(nn)