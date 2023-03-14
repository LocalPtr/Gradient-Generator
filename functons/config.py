import json
import dearpygui.dearpygui as dpg
import functons as func
import webbrowser
import os
from data import language
from functons.handler import set_custom_mode
from functons.items_edit import set_logic


def save():
    data = {
        'image_size': dpg.get_value('image_size'),
        'custom_size_width': dpg.get_value('custom_size_width'),
        'custom_size_height': dpg.get_value('custom_size_height'),
        'iterations': dpg.get_value('iterations'),
        'mutation': dpg.get_value('mutation'),
        'min_color_offset': dpg.get_value('min_color_offset'),
        'max_color_offset': dpg.get_value('max_color_offset'),
        'quality': dpg.get_value('quality'),
        'start': dpg.get_value('start'),
        'stop': dpg.get_value('stop'),
        'is_horizontal': dpg.get_value('is_horizontal'),
        'create_video': dpg.get_value('create_video'),
        'fps': dpg.get_value('fps'),
        'video_name': dpg.get_value('video_name'),
        'auto_title': dpg.get_value('auto_title'),
        'language': dpg.get_value('language'),
        'mode': dpg.get_value('mode'),
        'clear_junk': dpg.get_value('clear_junk'),
        'transition': dpg.get_value('transition')
    }
    json_data = json.dumps(data, sort_keys=True, indent=4)
    with open("config.json", "w") as my_file:
        my_file.write(json_data)


def reset():
    dpg.set_value('image_size', func.calculate.get_screen_size_str())
    dpg.set_value('custom_size_width', 500)
    dpg.set_value('custom_size_height', 500)
    dpg.set_value('iterations', 100)
    dpg.set_value('mutation', 20)
    dpg.set_value('min_color_offset', 1)
    dpg.set_value('max_color_offset', 15)
    dpg.set_value('quality', 90)
    dpg.set_value('start', True)
    dpg.set_value('stop', False)
    dpg.set_value('is_horizontal', False)
    dpg.set_value('create_video', True)
    dpg.set_value('fps', 20)
    dpg.set_value('video_name', 'video')
    dpg.set_value('auto_title', False)
    dpg.set_value('clear_junk', False)
    set_custom_mode()
    set_logic()


def open_folder():
    if dpg.get_value('create_video'):
        return webbrowser.open(f'{os.getcwd()}/My videos')
    return webbrowser.open(f'{os.getcwd()}/My images')


def load_language(lang):
    lang_id = {'English': 0, 'Русский': 1}
    dpg.set_item_label('image_size', language.pixel_size[lang_id.get(lang)])
    dpg.set_item_label('custom_size_width', language.width[lang_id.get(lang)])
    dpg.set_item_label('custom_size_height', language.height[lang_id.get(lang)])
    dpg.set_item_label('iterations', language.images[lang_id.get(lang)])
    dpg.set_item_label('mutation', language.mutation[lang_id.get(lang)])
    dpg.set_item_label('min_color_offset', language.min_color_offset[lang_id.get(lang)])
    dpg.set_item_label('max_color_offset', language.max_color_offset[lang_id.get(lang)])
    dpg.set_item_label('quality', language.quality[lang_id.get(lang)])
    dpg.set_item_label('start', language.start[lang_id.get(lang)])
    dpg.set_item_label('stop', language.stop[lang_id.get(lang)])
    dpg.set_item_label('is_horizontal', language.horizontal[lang_id.get(lang)])
    dpg.set_item_label('create_video', language.create_video[lang_id.get(lang)])
    dpg.set_item_label('fps', language.fps[lang_id.get(lang)])
    dpg.set_item_label('video_name', language.name[lang_id.get(lang)])
    dpg.set_item_label('auto_title', language.auto[lang_id.get(lang)])
    dpg.set_item_label('language', language.language[lang_id.get(lang)])
    dpg.set_item_label('open_folder', language.open_folder[lang_id.get(lang)])
    dpg.set_item_label('run', language.run[lang_id.get(lang)])
    dpg.set_value('video_settings', language.video_settings[lang_id.get(lang)])
    dpg.set_value('images_settings', language.images_settings[lang_id.get(lang)])
    size = ['7680x4320', '3840x2160', '2560x1440', '1920x1080', '1280x720', '854x480', '640x360', '426x240', '1366x768',
            '1000x1000', '500x500', '1080x1920', language.reset_custom[lang_id.get(dpg.get_value('language'))]]
    dpg.configure_item('image_size', items=size)
    dpg.configure_item('mode', items=language.generate_mode[lang_id.get(dpg.get_value('language'))])
    dpg.configure_item('transition', items=language.transition_combo[lang_id.get(dpg.get_value('language'))])
    dpg.set_item_label('mode', language.mode[lang_id.get(lang)])
    dpg.set_item_label('transition', language.transition[lang_id.get(lang)])
    dpg.set_item_label('clear_junk', language.clear_junk[lang_id.get(lang)])
    set_custom_mode(True)


def load_language_callback(sender, app_data, user_data):
    load_language(app_data)


def load():
    with open("config.json", "r") as my_file:
        capitals_json = my_file.read()
    json_data = json.loads(capitals_json)
    dpg.set_value('image_size', json_data.get('image_size'))
    dpg.set_value('custom_size_width', int(json_data.get('custom_size_width')))
    dpg.set_value('custom_size_height', int(json_data.get('custom_size_height')))
    dpg.set_value('iterations', int(json_data.get('iterations')))
    dpg.set_value('mutation', int(json_data.get('mutation')))
    dpg.set_value('min_color_offset', int(json_data.get('min_color_offset')))
    dpg.set_value('max_color_offset', int(json_data.get('max_color_offset')))
    dpg.set_value('quality', int(json_data.get('quality')))
    dpg.set_value('start', bool(json_data.get('start')))
    dpg.set_value('stop', bool(json_data.get('stop')))
    dpg.set_value('is_horizontal', bool(json_data.get('is_horizontal')))
    dpg.set_value('create_video', bool(json_data.get('create_video')))
    dpg.set_value('fps', int(json_data.get('fps')))
    dpg.set_value('video_name', json_data.get('video_name'))
    dpg.set_value('auto_title', bool(json_data.get('auto_title')))
    dpg.set_value('clear_junk', bool(json_data.get('clear_junk')))
    dpg.set_value('language', json_data.get('language'))
    load_language(json_data.get('language'))
    set_logic()


def open_url(sender, app_data, user_data):
    return webbrowser.open('https://t.me/bysandj')
