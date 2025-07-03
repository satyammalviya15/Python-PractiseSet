""" 2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|> ''' """
from datetime import datetime
name=input("Enter Your Name")
dt=datetime.now().date()
letter=f'''
Dear {name},
You are selected!
{dt}'''
print(letter)
