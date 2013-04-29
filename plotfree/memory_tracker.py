import calendar
from datetime import datetime
import json
import psutil


def bytes_to_megabytes(bytes):
    return bytes / 1024.0 / 1024.0


def get_available_memory_mb():
    bytes = psutil.virtual_memory().available
    return bytes_to_megabytes(bytes)


def get_time_for_flot():
    now = datetime.now()
    return calendar.timegm(now.timetuple()) * 1000


class MemoryTracker(object):
    def __init__(self, filename):
        self.data_points = []
        self.filename = filename
        try:
            with open(self.filename, "r") as f:
                self.data_points = json.load(f)["data"]
        except IOError as e:
            pass

    def add_data_point(self):
        data_point = (get_time_for_flot(),
                      get_available_memory_mb())
        self.data_points.append(data_point)

    def dump(self, num_points=-1):
        points_to_dump = self.data_points

        if num_points != -1:
            points_to_dump = self.data_points[-num_points:]

        with open(self.filename, "w") as f:
            data = {"label": "Available Memory (MB)",
                    "data": points_to_dump}
            f.write(json.dumps(data))
