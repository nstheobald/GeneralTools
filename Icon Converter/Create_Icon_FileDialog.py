from tkinter import Tk, filedialog as fld
import os
from Create_Icon import create_icon

root = Tk()
root.withdraw()
file_convert = fld.askopenfilename()
save_as = fld.asksaveasfile(title='Save As', initialdir=os.path.dirname(file_convert), defaultextension='.ico')
root.destroy()

create_icon(file_convert, save_as.name)
