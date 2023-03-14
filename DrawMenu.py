import dearpygui.dearpygui as dpg
import os

import functons as func
import data as d
import run

dpg.create_context()
size_height = 675
size_width = 600


def first_open():
    try:
        os.mkdir(f'{os.getcwd()}\\My images')
        os.mkdir(f'{os.getcwd()}\\My videos')
        os.mkdir(f'{os.getcwd()}\\junk')
    except FileExistsError:
        pass


with dpg.font_registry():
    ubuntu = '/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf'
    windows = 'C:/Windows/Fonts/calibri.ttf'
    with dpg.font(windows, 20, default_font=True, id="Default font"):
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        # remapping capital and small "ё"
        dpg.add_char_remap(0xa8, 0x401)
        dpg.add_char_remap(0xb8, 0x451)
        # set counter value equal to utf8 code of Russian capital "А" with consequent remapping from "А" to "я"
        utf = 0x410
        for i in range(0xc0, 0x100):
            dpg.add_char_remap(i, utf)
            utf += 1
    dpg.bind_font("Default font")

with dpg.texture_registry():
    dpg.add_static_texture(width=d.img.width_link_btn, height=d.img.height_link_btn, default_value=d.img.data_link_btn,
                           tag="Texture_link")
    dpg.add_static_texture(width=d.img.width_save_btn, height=d.img.height_save_btn,
                           default_value=d.img.data_save_btn,
                           tag="Texture_save")
    dpg.add_static_texture(width=d.img.width_reset_btn, height=d.img.height_reset_btn,
                           default_value=d.img.data_reset_btn, tag="Texture_reset")


def add_info_text(sign, message, color_sign: tuple = (182, 182, 182), color_text: tuple = (255, 255, 255)):
    last_item = dpg.last_item()
    group = dpg.add_group(horizontal=True)
    dpg.move_item(last_item, parent=group)
    dpg.capture_next_item(lambda s: dpg.move_item(s, parent=group))
    t = dpg.add_text(sign, color=color_sign)
    with dpg.tooltip(t):
        dpg.add_text(message, color=color_text)


with dpg.window(tag="Primary Window", autosize=True):
    first_open()
    dpg.add_combo(['7680x4320', '3840x2160', '2560x1440', '1920x1080', '1280x720', '854x480', '640x360', '426x240',
                   '1366x768', '1000x1000', '500x500', '1080x1920', 'Custom'],
                  default_value=func.calculate.get_screen_size_str(), label='Size', tag='image_size',
                  callback=func.items_edit.size)
    with dpg.group(horizontal=True):
        dpg.add_input_int(label='Width', width=150, tag='custom_size_width', show=False, default_value=500,
                          callback=func.handler.limit, user_data='1 50000')
        dpg.add_input_int(label='Height', width=150, tag='custom_size_height', show=False, default_value=500,
                          callback=func.handler.limit, user_data='1 50000')
    with dpg.group(horizontal=True):
        with dpg.child_window(width=570, height=255):
            with dpg.group(horizontal=True):
                dpg.add_text('Image setting', tag='images_settings')
                dpg.add_combo(['Custom', 'Smooth', 'Random'], default_value='Smooth transition',
                              tag='transition', width=200, label='Transition', callback=func.handler.images_type,
                              show=False)
            dpg.add_slider_int(label='Images', default_value=100, min_value=1, max_value=5000, tag='iterations',
                               user_data='1 7000', callback=func.handler.limit)
            dpg.add_slider_int(label='Mutation', default_value=15, min_value=0, max_value=100, tag='mutation',
                               callback=func.handler.mutation_limit, format="%d%%")
            dpg.add_slider_int(label='Min color offset', default_value=5, min_value=0, max_value=50,
                               tag='min_color_offset', callback=func.handler.min_color_offset_limit)
            dpg.add_slider_int(label='Max color offset', default_value=5, min_value=0, max_value=50,
                               tag='max_color_offset', callback=func.handler.max_color_offset_limit)
            dpg.add_slider_int(label='Quality', default_value=90, min_value=1, max_value=500, tag='quality',
                               user_data='1 5000', callback=func.handler.limit)
            with dpg.group(horizontal=True):
                dpg.add_checkbox(label='Start', tag='start', default_value=True)
                dpg.add_checkbox(label='Stop', tag='stop', default_value=False)
                dpg.add_checkbox(label='Horizontal', tag='is_horizontal', default_value=False)
            dpg.add_combo(d.language.generate_mode[0], label='Mode', default_value='Normal',
                          callback=func.handler.set_mode, tag='mode')
    with dpg.group(horizontal=True):
        with dpg.child_window(width=570, height=140):
            with dpg.group(horizontal=True):
                dpg.add_text('Video setting', tag='video_settings')
                dpg.add_checkbox(label='Create video', default_value=True, tag='create_video',
                                 callback=func.handler.transition)
            dpg.add_checkbox(label='Clear junk data after completion', default_value=False, tag='clear_junk')
            dpg.add_slider_int(label='FPS', default_value=20, min_value=1, max_value=200, tag='fps',
                               user_data='1 200', callback=func.handler.limit)
            with dpg.group(horizontal=True):
                dpg.add_input_text(label='Title', default_value='video', tag='video_name')
                dpg.add_checkbox(label='Auto', tag='auto_title')
    with dpg.group(horizontal=True):
        with dpg.child_window(width=570, height=50):
            with dpg.group(horizontal=True):
                dpg.add_image_button('Texture_save', callback=func.config.save)
                dpg.add_image_button('Texture_reset', callback=func.config.reset)
                dpg.add_image_button('Texture_link', callback=func.config.open_url)
                dpg.add_button(label='Open folder', width=200, height=30, callback=func.config.open_folder,
                               tag='open_folder')
                dpg.add_combo(['English', 'Русский'], label='Language', tag='language', width=170,
                              callback=func.config.load_language_callback)
    dpg.add_button(label='Run', width=570, height=40, callback=run.starting, tag='run')
    dpg.add_progress_bar(label='', tag='progress_bar', width=570, show=False)
    dpg.add_text('', tag='status')
    try:
        func.config.load()
    except FileNotFoundError:
        func.config.reset()
        dpg.set_value('language', 'English')

dpg.create_viewport(title='GradGenerator v1.1', width=size_width, height=size_height, max_width=size_width,
                    min_width=size_width, max_height=size_height, min_height=size_height, large_icon='img/logo.ico')

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
