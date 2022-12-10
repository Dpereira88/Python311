"""
File: test1_read_document.py
Project: Python311
File Created: Sat 10th Dec 2022 7:41:42 pm
Author: Dpereira88
"""



# Open the file 'myfile.txt' in read-only mode
with open('Requirements.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()
    # Print the contents of the file
    print(contents)