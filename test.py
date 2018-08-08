a = 112313
b = 1241

def test():
    print(a)
    b=2312

def x():
    print(b)

def y():
    global  b
    print(b)
    b ='aaaaa'

if __name__ == "__main__":
    test()
    x()