import calendar
from datetime import datetime


def bytes_to_megabytes(bytes):
    return bytes / 1024.0 / 1024.0


def bytes_to_gigabytes(bytes):
    return bytes_to_megabytes(bytes) / 1024.0


def get_time_for_flot():
    now = datetime.now()
    return calendar.timegm(now.timetuple()) * 1000
