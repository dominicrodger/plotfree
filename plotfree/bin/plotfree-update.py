#!/usr/bin/env python
from plotfree.disk_tracker import DiskTracker
from plotfree.memory_tracker import MemoryTracker
from plotfree.process_monitor import dump_processes
from plotfree.util import update_and_dump


if __name__ == "__main__":
    update_and_dump(MemoryTracker("public_html/data/memory.json"))
    update_and_dump(DiskTracker("public_html/data/disk.json"))
    dump_processes("public_html/data/processes.json")
