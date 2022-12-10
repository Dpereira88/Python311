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

#get the line number of the last cell empty from one given column
def get_empty_line(_cells, start_line, _column):
    value = 0
    count = 0
    while value is not None:
        count += 1
        value = _cells(count, _column).Value       
    return count

#clear cells given a start line and column and a end line and column
def clear_cells(_cells, start_line, end_line , start_column, end_column):
    end_line += 1
    end_column = chr(ord(end_column) + 1)
    _column = start_column
    while _column != end_column:
        _line = start_line
        while _line != end_line:
            _cells(_line, _column).Value = None 
            _line += 1
        _column = chr(ord(_column) + 1) # Increment the character by 1


try:
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = openWorkbook(excel, "Livro1.xlsx")
    ws = wb.Worksheets('Sheet1') 
    excel.Visible = True
    cells = ws.Cells
    #write code here
    #cells(6,"A").Value = "OK"  
    
    #get the last line from a given column
    number_empty_line = get_empty_line(cells, 1, "A")
    print(number_empty_line)
    
    #clear cells(cells, start_line, end_line , start_column, end_column) 
    clear_cells(cells, 1, 1, "A", "D")
    
    

except Exception as e:
    print(e)

finally:
    # RELEASES RESOURCES
    ws = None
    wb = None
    excel = None