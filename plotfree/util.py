import calendar
from datetime import datetime
import psutil


def bytes_to_megabytes(bytes):
    return bytes / 1024.0 / 1024.0


def get_available_memory_mb():
    bytes = psutil.virtual_memory().available
    return bytes_to_megabytes(bytes)


def get_time_for_flot():
    now = datetime.now()
    return calendar.timegm(now.timetuple()) * 1000
