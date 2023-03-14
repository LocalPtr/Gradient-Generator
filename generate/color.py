from random import randint
import dearpygui.dearpygui as dpg
from random import choices


def move(color: list, mutation_weight):
    bool_data = color[0]
    int_data = color[1]
    count = randint(dpg.get_value('min_color_offset'), dpg.get_value('max_color_offset'))
    if choices([False, True], weights=mutation_weight, k=1)[0]:
        bool_data = not bool_data
    if bool_data and int_data + count >= 255 or int_data >= 255:
        bool_data = not bool_data
    if not bool_data and int_data - count <= 0 or int_data <= 0:
        bool_data = not bool_data
    return [bool_data, int_data + count] if bool_data is True else [bool_data, int_data - count]


def randomizer():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return [red, green, blue]
