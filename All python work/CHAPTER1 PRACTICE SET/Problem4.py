import os

# Correct folder path
directory_path = '/'

# get contents
contents = os.listdir(directory_path)

# print contents
for item in contents:
    print(item)