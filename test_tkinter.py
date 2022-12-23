import tkinter as tk
from tkinter import filedialog
import os

# Create the main window
window = tk.Tk()
window.title("Input Window")

def select_file():
    # Display the file selection dialog
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

    # Display the selected file path
    print(file_path)

# Define the function for the "Cancel" button
def close_window():
    # Close the window and exit the program
    window.destroy()
    exit()

# Define the function for the "Open Folder" button
def open_folder():
    # Get the path from the input field
    path = input2.get()

    # Open the folder
    if os.path.isdir(path):
        os.startfile(path)
    else:
        print("Invalid path")



# Create the input fields and buttons
label1 = tk.Label(window, text="Bardoce:")
input1 = tk.Entry(window)
label2 = tk.Label(window, text="Link:")
input2 = tk.Entry(window)
input3 = tk.Entry(window)
upload_button = tk.Button(window, text="Upload", command=select_file)
ok_button = tk.Button(window, text="OK")
cancel_button = tk.Button(window, text="Cancel", command=close_window)
open_folder_button = tk.Button(window, text="Open Folder", command=open_folder)

# Place the widgets in a grid layout
label1.grid(row=0, column=0)
input1.grid(row=0, column=1)
label2.grid(row=1, column=0)
input2.grid(row=1, column=1)
input3.grid(row=2, column=0)
upload_button.grid(row=3, column=0)
ok_button.grid(row=3, column=1)
cancel_button.grid(row=3, column=2)
open_folder_button.grid(row=1, column=2)

# Define the function for the "Upload" button


# Run the main loop
window.mainloop()
