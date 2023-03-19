file=open("file2.txt","w+")
file.write("this is file w+ mode using python for read/write data.")
print(file.tell())
file.seek(0)
print(file.read())
file.close()
print("************************************************************")



file=open("file2.txt","r+")
print(file.read())
print(file.tell())
file.seek(0)
file.write("\nnow this is r+ mode in new line.")
file.close()
print("************************************************************")
