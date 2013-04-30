from .base_tracker import BaseTracker
from .util import get_available_memory_mb


class MemoryTracker(BaseTracker):
    data_label = "Available Memory (MB)"

    def get_data_point(self):
        return get_available_memory_mb()
