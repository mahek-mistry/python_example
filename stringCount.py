s=input("Enter A String : ")

wd=1
ch=0
sp=0
dt=0
sc=0

for i in s:
    if i.isalpha():
        ch=ch+1
    elif i.isspace():
        sp=sp+1
        wd=wd+1
    elif i.isnumeric():
        dt=dt+1
    else:
        sc=sc+1

print("Total Words : ",wd)
print("Total Character : ",ch)
print("Total Space : ",sp)
print("Total Digit: ",dt)
print("Total Special: ",sc)
