from dearpygui.dearpygui import *
import requests

from resources.variables import *

from ui import Window, NavBar


def dragViewport():
    drag_deltas = get_mouse_drag_delta()
    viewport_current_pos = get_viewport_pos()
    set_viewport_pos([viewport_current_pos[0] + drag_deltas[0], viewport_current_pos[1] + drag_deltas[1]])


def start_app():
    create_context()

    with font_registry():
        try:
            default_font = add_font("C:\Windows\Fonts\calibri.ttf", 15)
            bind_font(default_font)
        except:
            pass
    create_viewport(title=Product.Name,
                    width=750, height=430,
                    resizable=False,
                    decorated=False)

    with handler_registry():
        add_mouse_drag_handler(callback=dragViewport)

    setup_dearpygui()
    Window.show()

    show_viewport()
    start_dearpygui()
    destroy_context()


if __name__ == '__main__':
    start_app()
