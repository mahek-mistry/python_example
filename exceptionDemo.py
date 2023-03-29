print("start code")

try:
    
    a=int(input("enter A:"))
    b=int(input("enter B:"))

    c=a/b

    print("division: ",c)

    l=[1,2,3,4,5]
    index=int(input("enter index number: "))
    print(l[index])
except Exception as e:
    print("Exception caught : ",e)

print("end code")
