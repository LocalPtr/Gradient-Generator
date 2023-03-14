from random import choice
import dearpygui.dearpygui as dpg
from generate.images import create_only_images
from generate.video import create_video


def starting(sender, app_data, user_data):
    dpg.disable_item('run')
    if dpg.get_value('auto_title'):
        dpg.configure_item('video_name', readonly=True)
    dpg.show_item('progress_bar')
    match dpg.get_value('create_video'):
        case True:
            create_video()
        case False:
            create_only_images()
    dpg.set_value('status', "")
    dpg.configure_item('video_name', readonly=False)
    dpg.enable_item('run')
