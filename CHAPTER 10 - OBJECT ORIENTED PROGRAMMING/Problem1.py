# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    def __init__(self):
        self.name=input("Enter Programmer Name : ")
        self.language=input("Enter Your Programming Language : ")
        self.sallary=input("Enter Your Sallary : ")
    def printinfo(self):
        print(self.name,self.language,self.sallary)

satyam=Programmer()
satyam.printinfo()