from dearpygui.dearpygui import *

from resources.variables import *

from ui import NavBar

from backend import FileDialog
from backend import Converter


def show():
    with window(tag=Tag.PrimaryWindow):
        set_primary_window(Tag.PrimaryWindow, True)
        add_text("")  # Placeholder
        NavBar.show()

        with group(horizontal=True):
            with child_window(border=True, width=734, height=70):
                add_text("Input")

                with group(horizontal=True):
                    add_text("File Path    ")
                    add_input_text(tag=Tag.FileInput, no_spaces=True, width=530)
                    add_button(width=80, label="Browse", callback=FileDialog.input_file, tag=Tag.FileInputBrowseButton)

        with child_window(border=True, width=734, height=320):
            with group(horizontal=True):
                add_text("Output Path")
                add_input_text(tag=Tag.FileOutput, no_spaces=True, width=530)
                add_button(width=80, label="Browse", callback=FileDialog.output_dir, tag=Tag.DirectoryOutputBrowseButton)

            with group(horizontal=True):
                add_text("Filename    ")
                add_input_text(tag=Tag.FileName, no_spaces=True, width=460)

                add_text('Format')
                add_combo(tag=Tag.FormatCombo, items=Combo.Format, width=100, default_value=Combo.Format[0])

            add_separator()

            with child_window(tag=Tag.LogChild, border=False, width=530 + 460, height=220, no_scrollbar=False):
                # add_input_text(tag=Tag.LogOutput, multiline=True, width=715, height=220, enabled=False)
                Converter.info()

            add_separator()

            with group(tag=Tag.ConvertGroup, horizontal=True):
                add_button(width=100, label="Convert", callback=Converter.convert, tag=Tag.ConvertButton)

                add_progress_bar(default_value=0.0, width=610, tag=Tag.ConvertProgressBar)
