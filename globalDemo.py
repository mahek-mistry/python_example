global x

x=10

def test1():
    global y
    y=20
    print("x : ",x,"y : ",y)
    y=y+20

def test2():
    print("x : ",x,"y : ",y)

test1()
test2()
