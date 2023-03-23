class Student:

    def getData(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def putData(self):
        print("first name:",self.fname)
        print("last name:",self.lname)


s1=Student()
s2=Student()

s1.getData("mahek","mistry")
s1.putData()
