import dearpygui.dearpygui as dpg
from data.language import reset_custom


def size(sender, app_data, user_data):
    if app_data in reset_custom:
        dpg.show_item('custom_size_width')
        dpg.show_item('custom_size_height')
    else:
        dpg.hide_item('custom_size_width')
        dpg.hide_item('custom_size_height')


def set_logic():
    if dpg.get_value('image_size') in reset_custom:
        dpg.show_item('custom_size_width')
        dpg.show_item('custom_size_height')
    else:
        dpg.hide_item('custom_size_width')
        dpg.hide_item('custom_size_height')
    if dpg.get_value('create_video'):
        dpg.hide_item('transition')
    else:
        dpg.show_item('transition')

