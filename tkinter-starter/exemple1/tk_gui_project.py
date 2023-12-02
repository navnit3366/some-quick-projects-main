#                         #
#    by AGOSSOU Hermann   #
#                         #
'''A simple template for an tkinter i/o program with tkinter'''

# import the module and all specifications
# pip install tkinter
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import askopenfile

# create the window and set geometry and title
root = Tk()
root.geometry("500x500")
root.title("Welcome !!!")


# creating the commanding
# function of the button
def add_info():
    '''fonction1: get then override texte value'''
    textcontent = get_text()
    newText = get_new_text(textcontent)
    set_text(newText)


def download_data():
    '''fonction2: upload a file and override texte value'''
    #download file
    filepath = open_file()
    set_text(filepath)


def get_new_text(textcontent, **args):
    '''customisable method to handle content overriding'''
    return 'bof\nbof'


def open_file():
    '''handle upload and get filepath '''
    filepath = askopenfile(mode='r', filetypes=[("All files", "*.*")])
    return filepath


# create a label
label = Label(root,
              text="You can either add information or send an excel sheet")

# placing the label at the right position
label.place(x=100, y=80)

# create a button
button = Button(root, text="Add your info", command=add_info, bg="green")
button.place(x=130, y=130)

# create a button
button = Button(root,
                text="Download and analyse",
                command=download_data,
                bg="green")
button.place(x=250, y=130)

# create a textarea
# geometry
textarea = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=15)
textarea.grid(
    column=0,
    pady=10,
    padx=10,
)
textarea.place(x=90, y=240)
# get value
get_text = lambda: textarea.get('1.0', 'end')
# add text
set_text = lambda str: textarea.insert('1.0', str)

if __name__ == '__main__':
    # app mainloop
    root.mainloop()
