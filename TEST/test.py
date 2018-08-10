a = 112313
b = 1241

def test():
    print(a)
    b=2312

def x():
    print(b)

def y():
    global  b
    global  a
    a.append(2)
    print(b)
    b ='aaaaa'


def var(_1553b):
        global  a
        a = _1553b
        y()
        print(_1553b)
        def x():
            a.append(34)
        print(a)
if __name__ == "__main__":
    var([123,456])
    a = [1]
    b = [1,2]
    print(a==[1])