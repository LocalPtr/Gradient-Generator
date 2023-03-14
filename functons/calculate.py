import pyautogui
import dearpygui.dearpygui as dpg

from data.language import reset_custom


def get_screen_size_str():
    width, height = pyautogui.size()
    return f'{width}x{height}'


def get_screen_size():
    width, height = pyautogui.size()
    return [width, height]


def get_size_from_combo():
    size = dpg.get_value('image_size')
    if size not in reset_custom:
        w_size = size.split('x')
        return [int(w_size[0]), int(w_size[1])]
    return [dpg.get_value('custom_size_width'), dpg.get_value('custom_size_height')]
