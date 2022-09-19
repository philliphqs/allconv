import os

from dearpygui.dearpygui import *

class Product:
    Name = "allconv"
    Version = "0.0.1-alpha"
    Author = "philliphqs"


class URL:
    GitHub = f"https://github.com/{Product.Author}/{Product.Name}"
    GitHubReleases = f"{GitHub}/releases"
    GitHubLatestRelease = f"{GitHubReleases}/latest"
    GitHubLatestReleaseDownload = f"{GitHubLatestRelease}/download"

    Website = f"https://{Product.Author}.github.io/{Product.Name}"
    Help = f"{Website}/help"


class Path:
    FFMPEG = './ffmpeg/ffmpeg.exe'
    Resources = "resources/"
    Icons = f"{Resources}icons/"
    Ads = f"{Resources}ads/"
    Screenshots = f"{Resources}screenshots/"
    Fonts = f"{Resources}fonts/"


class File:
    class JSON:
        Language = f"{Path.Resources}language.json"

    class Icons:
        Icon = Path.Icons + "product_icons/icon.ico"

    class Images:
        Icon = [rf"C:\Program Files (x86)\allconv\icon.png",  # Path
                "icon.png",     # Name
                "https://raw.githubusercontent.com/philliphqs/allconv/main/resources/icons/product_icons/icon.png"]  # URL


class Tag:
    DirectoryOutputBrowseButton = "directory_output_browse_button"
    FileInputBrowseButton = "file_input_browse_button"
    ConvertButton = "convert_button"
    ConvertProgressBar = "convert_progress_bar"
    ConvertGroup = "convert_group"
    LogChild = "log_child"
    LogOutput = "log_output"
    FileName = "file_name"
    FileOutput = "file_output"
    FileInput = "file_input"
    FormatCombo = "format_combo"
    TitleInput = "title_input"
    PathInput = "path_input"
    PrimaryWindow = "primary_window"


class Combo:
    Format = ['.mp4', '.mov', '.webm', '.gif', '.avi', '.vob']
    FileTypes = [('Video Files', '*.mp4 *.mov *.webm *.gif *.avi *.vob')]


class Fonts:
    Arial = Path.Fonts + "arial.ttf"