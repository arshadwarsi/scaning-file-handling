import tkinter as tk
from tkinter import filedialog
import csv

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        process_csv(file_path)

def process_csv(file_path):
    data = []
    duplicates = set()
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Assuming the first row is the header
        
        for row in csvreader:
            if tuple(row) in data:
                duplicates.add(tuple(row))
            else:
                data.append(tuple(row))

    if duplicates:
        display_duplicates(duplicates)
    else:
        display_message("No duplicates found.")

def display_duplicates(duplicates):
    duplicate_window = tk.Toplevel(root)
    duplicate_window.title("Duplicate Values")
    
    listbox = tk.Listbox(duplicate_window)
    listbox.pack()
    
    for item in duplicates:
        listbox.insert(tk.END, item)

def display_message(message):
    messagebox.showinfo("Message", message)

# Create the main application window
root = tk.Tk()
root.title("CSV Data Scanner")

# Create and pack UI elements
browse_button = tk.Button(root, text="Browse CSV File", command=browse_file)
browse_button.pack()

# Start the Tkinter main loop
root.mainloop()
