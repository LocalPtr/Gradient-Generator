import numpy as np
from random import randint, choices
from PIL import Image
import dearpygui.dearpygui as dpg
from data import language

import functons.date_time
from functons.calculate import get_size_from_combo
from generate.color import move, randomizer

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


def create_only_images():
    min_number = dpg.get_value('min_color_offset')
    max_number = 255 - dpg.get_value('max_color_offset') + min_number
    red_1 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    red_2 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    green_1 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    green_2 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    blue_1 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    blue_2 = [boolean_lst[randint(0, 1)], randint(min_number, max_number)]
    size_width, size_height = get_size_from_combo()[0], get_size_from_combo()[1]
    text = language.generate_images.get(dpg.get_value('language'))
    start = dpg.get_value('start')
    stop = dpg.get_value('stop')
    horizontal = dpg.get_value('is_horizontal')
    quality = dpg.get_value('quality')
    percent = dpg.get_value('mutation') / 100
    weight_lst = [1 - percent, percent]
    for i in range(dpg.get_value('iterations') + 1):
        dpg.set_value('progress_bar', i / dpg.get_value('iterations'))
        dpg.configure_item('progress_bar', overlay=f"{text} [{i}/{dpg.get_value('iterations')}]")
        #red_1 = move(red_1, weight_lst)
        #red_2 = move(red_2, weight_lst)
        #green_1 = move(green_1, weight_lst)
        #green_2 = move(green_2, weight_lst)
        #blue_1 = move(blue_1, weight_lst)
        #blue_2 = move(blue_2, weight_lst)
        red_1[1], blue_1[1], green_1[1] = randomizer()
        red_2[1], blue_2[1], green_2[1] = randomizer()
        array = get_gradient_3d(size_width, size_height, (red_1[1], green_1[1], blue_1[1]),
                                (red_2[1], green_2[1], blue_2[1]),
                                (start, stop, horizontal))
        Image.fromarray(np.uint8(array)).save(f'My images/img-{functons.date_time.now()}.jpg',
                                              quality=quality)
    dpg.hide_item('progress_bar')
