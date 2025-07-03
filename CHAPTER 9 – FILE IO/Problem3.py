# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
def multi_table():
    table=""
    for i in range(2,21):
        line=f"\nTable of {i}\n"
        table+=line
        for j in range(1,11):
            line = f"{i} * {j} = {i*j}\n"
            table +=line
    return table

with open("multitable.txt","w") as f:
    f.write(multi_table())