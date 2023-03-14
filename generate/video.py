import numpy as np
from random import randint
import re
from random import choice, choices
import moviepy.video.io.ImageSequenceClip
from PIL import Image, ImageFile
import dearpygui.dearpygui as dpg
from data import language
from functons.handler import drs
from functons import date_time
from functons.calculate import get_size_from_combo
from generate.color import move
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True
boolean_lst = [True, False]


def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros([height, width, len(start_list)])

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result


def create_video():
    min_number = dpg.get_value('min_color_offset')
    max_number = 255 - dpg.get_value('max_color_offset') + min_number
    red_1 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    red_2 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    green_1 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    green_2 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    blue_1 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    blue_2 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    image_files = []
    size_width, size_height = get_size_from_combo()[0], get_size_from_combo()[1]
    text = language.generate_images.get(dpg.get_value('language'))
    start = dpg.get_value('start')
    stop = dpg.get_value('stop')
    horizontal = dpg.get_value('is_horizontal')
    quality = dpg.get_value('quality')
    fps = dpg.get_value('fps')
    old_video_name = drs(dpg.get_value('video_name'))
    clear_junk = dpg.get_value('clear_junk')
    info_cleaning = language.cleaning.get(dpg.get_value('language'))
    if dpg.get_value('auto_title'):
        video_name = old_video_name
        for i in range(12):
            video_name += ''.join(choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))
        dpg.set_value('video_name', video_name)
    else:
        video_name = old_video_name
    percent = dpg.get_value('mutation') / 100
    weight_lst = [1 - percent, percent]
    start_time = date_time.now()
    for i in range(dpg.get_value('iterations') + 1):
        dpg.set_value('progress_bar', i / dpg.get_value('iterations'))
        dpg.configure_item('progress_bar', overlay=f"{text} [{i}/{dpg.get_value('iterations')}]")
        red_1 = move(red_1, weight_lst)
        red_2 = move(red_2, weight_lst)
        green_1 = move(green_1, weight_lst)
        green_2 = move(green_2, weight_lst)
        blue_1 = move(blue_1, weight_lst)
        blue_2 = move(blue_2, weight_lst)
        array = get_gradient_3d(size_width, size_height, (red_1[1], green_1[1], blue_1[1]),
                                (red_2[1], green_2[1], blue_2[1]),
                                (start, stop, horizontal))
        Image.fromarray(np.uint8(array)).save(f'junk/img-{i}.jpg', quality=quality)
        image_files.append(f'junk/img-{i}.jpg')
    dpg.hide_item('progress_bar')
    dpg.set_value('status', language.reading_for_create_video.get(dpg.get_value('language')))
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    end_time = date_time.changed_time(date_time.time_difference(start_time))
    dpg.set_value('status', f"{language.creating_video.get(dpg.get_value('language'))} "
                            f"{re.split(r'[ .]', str(end_time))[1]}")
    clip.write_videofile(f'My videos/{video_name}.mp4')
    dpg.set_value('video_name', old_video_name)
    if clear_junk:
        dpg.set_value('status', info_cleaning)
        for file_name in os.listdir(f'{os.getcwd()}\\junk'):
            file = f'{os.getcwd()}\\junk\\' + file_name
            if os.path.isfile(file):
                os.remove(file)
