# 11. Write a python program to rename a file to “renamed_by_ python.txt.
import os

old_name = "logfile.txt"
new_name = "renamed_by_python.txt"

# Rename the file
os.rename(old_name, new_name)

print(f"File renamed from {old_name} to {new_name}")