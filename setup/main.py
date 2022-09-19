import os, requests, zipfile, io, ctypes, sys, urllib.request

from dearpygui.dearpygui import *


class Product:
    Name = "allconv"
    Version = "0.0.1"
    Author = "philliphqs"


class Download:
    ZIPUrl = "https://github.com/philliphqs/allconv/archive/refs/heads/main.zip"


class Tag:
    LogOutput = "LogOutput"
    PrimaryWindow = "PrimaryWindow"
    NextButton = "NextButton"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def install():
    def log(text):
        add_text(text, parent=Tag.LogOutput)
        set_y_scroll(item=Tag.LogOutput, value=get_y_scroll_max(Tag.LogOutput) + 300)

    hide_item(item=Tag.NextButton)

    log("Downloading files...")
    r = requests.get(Download.ZIPUrl)
    log("Finished downloading files.")
    log("Extracting files...")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("C:/Program Files/")
    log("Finished extracting files.")

    log("Creating shortcuts...")

    with open(rf"C:\Users\{os.getenv('username')}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\allconv.bat",
              "w") as f:
        f.write('@echo off\n'
                'cd "C:/Program Files/allconv-main"\n'
                'python main.py')
        f.close()

    log("Finished creating shortcuts.")


def dragViewport():
    drag_deltas = get_mouse_drag_delta()
    viewport_current_pos = get_viewport_pos()
    set_viewport_pos([viewport_current_pos[0] + drag_deltas[0], viewport_current_pos[1] + drag_deltas[1]])


def show_navbar():
    with viewport_menu_bar():
        add_spacer(width=685)
        add_menu_item(label='_', callback=minimize_viewport)
        add_menu_item(label='X', callback=stop_dearpygui)


def show():
    with window(tag=Tag.PrimaryWindow):
        set_primary_window(Tag.PrimaryWindow, True)
        add_text("")  # Placeholder

        add_text(f"Welcome to the {Product.Name} Installer!")
        add_separator()
        add_text(f'This setup will install {Product.Name} on your computer.\n'
                 f'Click "Next" to continue, or Close this window to exit the setup.\n'
                 f'By clicking "Next", you agree to the terms of the End User License Agreement.\n')

        with child_window(tag=Tag.LogOutput, width=730, height=200):
            add_text("Log Output")

        add_separator()
        with group(horizontal=True):
            add_spacer(width=620)
            add_button(label="Next", callback=install, width=100, tag=Tag.NextButton)


if __name__ == '__main__':
    if is_admin():
        create_context()

        with font_registry():
            try:
                default_font = add_font("C:\Windows\Fonts\calibri.ttf", 15)
                bind_font(default_font)
            except:
                pass

        with handler_registry():
            add_mouse_drag_handler(callback=dragViewport)

        create_viewport(title=Product.Name,
                        width=750, height=350,
                        resizable=False,
                        decorated=False)
        setup_dearpygui()
        show()
        show_navbar()
        show_viewport()
        start_dearpygui()

        destroy_context()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
