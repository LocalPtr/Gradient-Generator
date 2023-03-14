import dearpygui.dearpygui as dpg
from data.language import reset_custom, reset_transition


def set_custom_mode(user: bool = False):
    lang_id = {'English': 0, 'Русский': 1}
    error_change_mode = ['Custom', 'Пользовательский']
    error_transition_mode = ['Smooth', 'Плавный']
    if user:
        change_mode = reset_custom[lang_id.get(dpg.get_value('language'))]
        transition_mode = reset_transition[lang_id.get(dpg.get_value('language'))]
    else:
        try:
            change_mode = error_change_mode[lang_id.get(dpg.get_value('language'))]
            transition_mode = error_transition_mode[lang_id.get(dpg.get_value('language'))]
        except TypeError:
            change_mode = 'Normal'
            transition_mode = 'Smooth'
    dpg.set_value('mode', change_mode)
    dpg.set_value('transition', transition_mode)


def min_color_offset_limit(sender, app_data, user_data):
    set_custom_mode(True)
    max_value = dpg.get_value('max_color_offset')
    if app_data > max_value:
        dpg.set_value('min_color_offset', max_value)
    elif app_data < 0:
        dpg.set_value('min_color_offset', 0)


def max_color_offset_limit(sender, app_data, user_data):
    set_custom_mode(True)
    min_value = dpg.get_value('min_color_offset')
    if app_data < min_value:
        dpg.set_value('max_color_offset', min_value)
    if app_data > 255 - min_value:
        dpg.set_value('max_color_offset', 255 - min_value)


def mutation_limit(sender, app_data, user_data):
    set_custom_mode(True)
    if app_data > 100:
        dpg.set_value('mutation', 100)
    if app_data < 0:
        dpg.set_value('mutation', 0)


def limit(sender, app_data, user_data):
    values = user_data.split(' ')
    min_value, max_value = int(values[0]), int(values[1])
    if app_data > max_value:
        dpg.set_value(sender, max_value)
    if app_data < min_value:
        dpg.set_value(sender, min_value)


def drs(text):
    # decode_russian_symbols
    # 848
    lower_case = [224, 255]
    upper_case = [192, 223]
    yo_bl = [168, 184]  # big - little
    # 1025 - 1105
    result = ''
    for i in text:
        if (lower_case[0] <= ord(i) <= lower_case[1]) or (upper_case[0] <= ord(i) <= upper_case[1]):
            result += f'{chr(ord(i) + 848)}'
        else:
            result += i
    return result


def set_mode(sender, app_data, user_data):
    mutation = 0
    min_offset = 0
    max_offset = 0
    match app_data:
        case 'Very smooth' | 'Очень плавный':
            mutation = 1
            min_offset = 0
            max_offset = 1
        case 'Smooth' | 'Плавный':
            mutation = 7
            min_offset = 0
            max_offset = 5
        case 'Normal' | 'Обычный':
            mutation = 20
            min_offset = 1
            max_offset = 15
        case 'Quick' | 'Быстрый':
            mutation = 20
            min_offset = 10
            max_offset = 20
        case 'Shake' | 'Трясущийся':
            mutation = 50
            min_offset = 15
            max_offset = 30
        case 'Broken' | 'Сломанный':
            mutation = 80
            min_offset = 50
            max_offset = 150
    dpg.set_value('mutation', mutation)
    dpg.set_value('min_color_offset', min_offset)
    dpg.set_value('max_color_offset', max_offset)


def transition(sender, app_data, user_data):
    if app_data:
        dpg.hide_item('transition')
        dpg.show_item('mutation')
        dpg.show_item('min_color_offset')
        dpg.show_item('max_color_offset')
        dpg.show_item('mode')
    else:
        dpg.show_item('transition')


def images_type(sender, app_data, user_data):
    match app_data:
        case 'Custom' | 'Пользовательский':
            dpg.hide_item('mutation')
            dpg.hide_item('min_color_offset')
            dpg.hide_item('max_color_offset')
            dpg.hide_item('mode')
        case 'Smooth' | 'Плавный':
            dpg.show_item('mutation')
            dpg.show_item('min_color_offset')
            dpg.show_item('max_color_offset')
            dpg.show_item('mode')
        case 'Random' | 'Случайный':
            dpg.hide_item('mutation')
            dpg.hide_item('min_color_offset')
            dpg.hide_item('max_color_offset')
            dpg.hide_item('mode')

