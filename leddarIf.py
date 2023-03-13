sname=input("enter student name:")
rno=input("enter student roll no:")
s1=int(input("enter marks of subject s1:"))
s2=int(input("enter marks of subject s2:"))
s3=int(input("enter marks of subject s3:"))

total=s1+s2+s3
per=total/3

print("student name:",sname)
print("student roll no:",rno)
print("total:",total)
print("percentage:",per)

if per>=70:
    print("districation")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
elif per>40:
    print("pass class")
else:
    print("fail")


