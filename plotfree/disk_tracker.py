import psutil
from .base_tracker import BaseTracker
from .util import bytes_to_gigabytes


class DiskTracker(BaseTracker):
    data_label = "Available Disk Space (GB)"

    def get_data_point(self):
        bytes = psutil.disk_usage('/').free
        return bytes_to_gigabytes(bytes)
