import dearpygui.dearpygui as dpg
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


txtr_link = resource_path("img\\link.png")
txtr_save = resource_path("img\\save.png")
txtr_reset = resource_path("img\\reset.png")


width_link_btn, height_link_btn, channels_link_btn, data_link_btn = dpg.load_image(txtr_link)
width_save_btn, height_save_btn, channels_save_btn, data_save_btn = dpg.load_image(txtr_save)
width_reset_btn, height_reset_btn, channels_reset_btn, data_reset_btn = dpg.load_image(txtr_reset)


