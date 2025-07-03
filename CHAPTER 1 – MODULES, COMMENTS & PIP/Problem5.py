# 5. Label the program written in problem 4 with comments. 
import os

# Specify the directory path (you can also use '.' for the current directory)
directory_path = '.'

# Get list of files and directories
contents = os.listdir(directory_path)

# Print each item in the directory
print(f"Contents of directory '{directory_path}':")
for item in contents:
    print(item)
