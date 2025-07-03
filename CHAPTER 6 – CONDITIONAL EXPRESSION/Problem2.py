# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
submarks=[]
subtotal=0
state=True
for i in range(3):
    sub = int(input(f"Enter The Marks of Subject{i+1} : "))
    subtotal+=sub
    submarks.append(sub)
for submark in submarks:
    if submark<33:
        state=False
        break
percentage = round((subtotal/300)*100,2)
if state==True and subtotal>=40:
    print(f"You are Pass in Examination with {percentage}%")
else:
    print("You are Fail in Examination")