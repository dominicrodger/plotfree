import calendar
from datetime import datetime


def bytes_to_megabytes(bytes):
    return bytes / 1024.0 / 1024.0


def bytes_to_gigabytes(bytes):
    return bytes_to_megabytes(bytes) / 1024.0


def get_time_for_flot():
    now = datetime.now()
    return calendar.timegm(now.timetuple()) * 1000


def update_and_dump(tracker):
    tracker.add_data_point()

    # Only dump the latest 1440 points - intended for half-hourly
    # stats for a month (2 * 24 * 30)
    tracker.dump(1440)
