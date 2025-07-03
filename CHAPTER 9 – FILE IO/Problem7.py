# 7. Write a program to find out the line number where python is present from ques 6.
with open("logfile.txt","r") as f:  
    for line_no,line in enumerate(f,start=1):
      if "python" in line.lower():
         print(line_no)