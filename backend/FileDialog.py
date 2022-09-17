from tkinter import filedialog
from dearpygui.dearpygui import *

from resources.variables import *


def input_file():
    filename = filedialog.askopenfilename(filetypes=Combo.FileTypes)
    set_value(Tag.FileInput, filename)


def output_dir():
    file_path = filedialog.askdirectory()
    set_value(Tag.FileOutput, file_path)
