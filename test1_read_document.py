"""
File: test1_read_document.py
Project: Python311
File Created: Sat 10th Dec 2022 7:41:42 pm
Author: Dpereira88
"""



def read_document(directory):
    # Open the file 'myfile.txt' in read-only mode
    with open(directory, 'r') as f:
        # Read the contents of the file
        contents = f.read()
        # Return the contents of the file
        return contents

def read_document_last_lines(directory, number_of_last_lines):
    # Open the file 'myfile.txt' in read-only mode
    with open(directory, 'r') as f:
        # Read the contents of the file
        contents = f.readlines()[-number_of_last_lines:]
        # Return the contents of the file
        return contents

# takes in a list of strings and returns
# a new list where each element is a list of strings, split from the original string by whitespace.
def convert_to_List_of_Lists(value):
    newList=[]
    # Loop over each element in the input list
    for x in value:
        # Split the element by whitespace and append the resulting list to newList
        newList.append(x.split())
    return newList


link_document = 'Requirements.txt'

value = read_document(link_document)

value = read_document_last_lines(link_document, 3)
print(value)
x = convert_to_List_of_Lists(value)
print(x)