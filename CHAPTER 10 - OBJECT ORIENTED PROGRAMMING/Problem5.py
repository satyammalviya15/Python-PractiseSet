# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
class Train:
    def __init__(self):
        self.train=[20255]
        self.seat=[2]
    def userinfo(self):
        self.username=input("Enter Your Name : ")
        self.userage=int(input("Enter Your age : "))
        self.usertrain=int(input("Enter Your Train No : "))
        for index,train in enumerate(self.train,start=0):
            if self.usertrain==train:
                self.train_no=train
                self.train_index=index
        if self.seat[self.train_index]>0:
            print("You Succesfully Book Ticket in Train No",self.train_no,"Seat No",self.seat[self.train_index])
            self.seat[self.train_index]-=1
        else:
            print("No seat is Avalible in Train",self.train_no)

user=Train()
user.userinfo()
user.userinfo()