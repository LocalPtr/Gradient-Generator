import datetime
from dateutil.relativedelta import relativedelta


def now() -> datetime.datetime.strftime:
    today = datetime.datetime.now()
    return today.strftime("%H-%M-%S-%f %d-%m-%Y")


def changed_time(time_lst: list):
    date_and_time = datetime.datetime.now()
    time_change = datetime.timedelta(hours=time_lst[0], minutes=time_lst[1], seconds=time_lst[2])
    new_time = date_and_time + time_change
    return new_time


def time_difference(time_now: str):
    try:
        start = datetime.datetime.strptime(time_now, "%H-%M-%S-%f %d-%m-%Y")
    except ValueError:
        start = datetime.datetime.strptime(now(), "%H-%M-%S-%f %d-%m-%Y")
    ends = datetime.datetime.strptime(now(), "%H-%M-%S-%f %d-%m-%Y")
    difference = relativedelta(ends, start)
    return [difference.hours, difference.minutes, difference.seconds]
