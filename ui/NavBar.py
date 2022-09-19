import ctypes
from dearpygui.dearpygui import *

from resources.variables import *

from backend import Interaction, Download


def stop_app():
    resp = ctypes.windll.user32.MessageBoxW(0,
                                            u"Are you sure you want to exit?",
                                            Product.Name, 4)
    if resp == 6:
        stop_dearpygui()
    else:
        pass


def show():
    with viewport_menu_bar():
        Download.download()
        width, height, channels, data = load_image(File.Images.Icon[0])
        with texture_registry():
            icon = add_static_texture(width, height, data)
        add_image(icon, width=20, height=20)

        with menu(label=Product.Name):
            with menu(label="About"):
                with group(horizontal=True):
                    try:
                        add_image(icon, width=80, height=80)
                    except:
                        add_spacer(width=80)
                    add_text(f'{Product.Name}\n'
                             f'Author: {Product.Author}\n')
                    add_text(Product.Version, bullet=True)

            add_separator()
            add_menu_item(label="GitHub", callback=Interaction.GitHub)
            add_menu_item(label="Website", callback=Interaction.Website)
            add_separator()
            add_menu_item(label="Exit", callback=stop_dearpygui)

        add_spacer(width=577)
        with menu(label="?"):
            add_menu_item(label="Report a bug", callback=Interaction.report_bug)
            add_menu_item(label="Request a feature", callback=Interaction.request_a_feature)
            add_separator()
            add_menu_item(label="Support", callback=Interaction.Help)

        add_menu_item(label='_', callback=minimize_viewport)
        add_menu_item(label='X', callback=stop_app)
