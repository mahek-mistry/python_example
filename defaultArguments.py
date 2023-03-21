
def test(a=20,b=30,c=40,d=50):
    print("A : ",a," B : ",b," C : ",c," D : ",d)

test(10,20,30,40)   
test(10,20,30)      

test(10,20)
test(10)
test()

test(30,40)         # a and b arguments taken and c and d takes default arguments

test(b=60,d=70)     # a and c value taken from default arguments
