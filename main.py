from tkinter import *
from tkinter.filedialog import asksaveasfilename

# Create the main window
stimulator_window = Tk()
stimulator_window.geometry('800x400')
stimulator_window.title('Text Editor v0.0.1-alpha')

heading = Label(stimulator_window, text="Welcome to the text editor",
                font=('bold', 20), bg='light grey')
heading.pack()

# Creating Text editor area and Scrollbar
scrollbar = Scrollbar(stimulator_window)
scrollbar.pack(side=RIGHT, fill=Y)

Editor = Text(stimulator_window, width=200, height=250, 
              yscrollcommand=scrollbar.set)
Editor.pack(fill=BOTH)

scrollbar.config(command=Editor.yview)

# Save() function
def save():
    filepath = asksaveasfilename(defaultextension="txt", 
                                 filetypes=[("Text Files", "*.txt"), 
                                            ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = Editor.get(1.0, END)
        output_file.write(text)
    stimulator_window.title(f"Entitled - {filepath}")

# Creating Buttons
button = Button(stimulator_window, text='Save', font=('normal', 10),
                command=save, bg='yellow')
button.pack()  # Use pack for layout management

# Command to run the main loop
stimulator_window.mainloop()

'''
I need to add some other features on to this. 
Google solutions for what to add.

Think about
'''