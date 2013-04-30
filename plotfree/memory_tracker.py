import psutil
from .base_tracker import BaseTracker
from .util import bytes_to_megabytes


class MemoryTracker(BaseTracker):
    data_label = "Available Memory (MB)"

    def get_data_point(self):
        bytes = psutil.virtual_memory().available
        return bytes_to_megabytes(bytes)
