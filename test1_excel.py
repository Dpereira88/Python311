"""
File: test1_excel.py
Project: Python311
File Created: Sat 10th Dec 2022 7:48:46 pm
Author: Dpereira88
"""



import win32com.client as win32

def openWorkbook(xlapp, xlfile):
    try:        
        xlwb = xlapp.Workbooks(xlfile)            
    except Exception as e:
        try:
            xlwb = xlapp.Workbooks.Open(xlfile)
        except Exception as e:
            print(e)
            xlwb = None                    
    return(xlwb)

def get_empty_line(_cells, start_line, _column):
    # Initialize the value and count variables
    value = 0
    count = start_line
    # Loop until we find a cell with a value of None
    while value is not None:
        count += 1
        value = _cells(count, _column).Value
    # Return the line number of the first empty cell
    return count

def clear_cells(_cells, start_line, end_line , start_column, end_column):
    # Increment the end coordinates by 1 to include the end cells in the range
    end_line += 1
    end_column = chr(ord(end_column) + 1)
    # Loop through each column in the specified range
    _column = start_column
    while _column != end_column:
        # Loop through each line in the specified range
        _line = start_line
        while _line != end_line:
            # Set the value of the cell at the given coordinates to None
            _cells(_line, _column).Value = None 
            _line += 1
        # Increment the column character by 1
        _column = chr(ord(_column) + 1)

def insert_values_from_list(_cells, list_w_Values, start_line, start_column):
    value = 0
    count = 0
    _line = start_line
    for line_values in list_w_Values:
        _column = start_column
        for column_value in line_values:
            _cells(_line,_column).Value = column_value
            _column = chr(ord(_column) + 1)
        _line += 1
        
        

try:
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = openWorkbook(excel, "C:\GitHub\Python311\Livro1.xlsx")
    ws = wb.Worksheets('Sheet1') 
    excel.Visible = True
    cells = ws.Cells
    #write code here
    #get the last line from a given column
    number_empty_line = get_empty_line(cells, 1, "A")
    #clear cells(cells, start_line, end_line , start_column, end_column) 
    #clear_cells(cells, 1, 1, "A", "D")
    list_values = [[1,2,3,4,5,6,7,8],["A","B","C","D","E"]]
    insert_values_from_list(cells, list_values, 6, "D")

except Exception as e:
    print(e)

finally:
    # RELEASES RESOURCES
    ws = None
    wb = None
    excel = None
