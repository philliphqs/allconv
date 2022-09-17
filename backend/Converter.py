import ctypes
import datetime
import threading

from dearpygui.dearpygui import *
import subprocess
import ffmpeg
import os

import cv2

from resources.variables import *


def disable_items():
    for item in [Tag.ConvertButton, Tag.FileInput, Tag.FileOutput, Tag.FileName,
                 Tag.FormatCombo, Tag.FileInputBrowseButton, Tag.DirectoryOutputBrowseButton]:
        disable_item(item)
        set_item_callback(item, callback=print)


def enable_items():
    for item in [Tag.ConvertButton, Tag.FileInput, Tag.FileOutput, Tag.FileName,
                 Tag.FormatCombo, Tag.FileInputBrowseButton, Tag.DirectoryOutputBrowseButton]:
        enable_item(item)


def info():
    output = subprocess.Popen('ffmpeg -version', stdout=subprocess.PIPE, shell=True).communicate()[0]
    # set_value(item=Tag.LogOutput, value=f'{Product.Name}, {Product.Version}\n'
    add_text(parent=Tag.LogChild, default_value=f'{Product.Name}, {Product.Version}\n'
                                                f'FFmpeg version: {output.decode("utf-8")}'
                                                f'This product is still in a beta so if something doesnt work please report it (click the ? to report)\n'
             )


def convert(status: None):
    def process():
        data = cv2.VideoCapture(get_value(Tag.FileInput))
        frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = data.get(cv2.CAP_PROP_FPS)

        seconds = round(frames / fps)
        video_time = datetime.timedelta(seconds=seconds)

        # set_value(value=get_value(Tag.LogOutput)+"\nConverting file...", item=Tag.LogOutput)
        add_text("Converting file...", parent=Tag.LogChild)
        cmd = f'ffmpeg -i ' + '"' + get_value(Tag.FileInput) + '"' + ' ' + '"' + get_value(
            Tag.FileOutput) + '/' + get_value(
            Tag.FileName) + get_value(Tag.FormatCombo) + '"'
        process_ = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        progress = 0.0
        set_value(Tag.ConvertProgressBar, progress)

        for line in process_.stdout:
            if "No such file or directory" in line:
                ctypes.windll.user32.MessageBoxW(0, u"Can't find required files! Check the path of your files.",
                                                 Product.Name + ' - Error', 0)
                set_value(Tag.ConvertProgressBar, 0.0)
                enable_items()
                return
            if "already exist" in line:
                ctypes.windll.user32.MessageBoxW(0, u"Filename already exist! Please change the filename.",
                                                 Product.Name + ' - Error', 0)
                set_value(Tag.ConvertProgressBar, 0.0)
                enable_items()
                return
            if "Invalid argument" in line:
                ctypes.windll.user32.MessageBoxW(0, u"Invalid argument! Please check your input.",
                                                 Product.Name + ' - Error', 0)
                set_value(Tag.ConvertProgressBar, 0.0)
                enable_items()
                return
            progress = progress + 0.001
            set_value(Tag.ConvertProgressBar, progress)

            add_text(line, parent=Tag.LogChild)
            print(get_value(Tag.ConvertProgressBar))

            # disable_items()
            set_y_scroll(item=Tag.LogChild, value=get_y_scroll_max(Tag.LogChild) + 300)

        set_value(Tag.ConvertProgressBar, 1.0)
        # enable_items()
        resp = ctypes.windll.user32.MessageBoxW(0,
                                                u"Conversion complete! Would you like to open the file?",
                                                Product.Name, 4)
        if resp == 6:
            os.system(
                "start " + get_value(Tag.FileOutput) + '/' + get_value(Tag.FileName) + get_value(Tag.FormatCombo))
        else:
            pass
        set_value(Tag.ConvertProgressBar, 0)

    x = threading.Thread(target=process)
    x.start()
