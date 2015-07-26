#!/usr/bin/env python
import click
import os

from plotfree.disk_tracker import DiskTracker
from plotfree.memory_tracker import MemoryTracker
from plotfree.process_monitor import dump_processes
from plotfree.util import update_and_dump


@click.command()
@click.option(
    "--path",
    default="",
    help="Path to folder containing your public_html directory."
)
def plotfree_update(path):
    data_path = os.path.join(path, "public_html/data/")
    update_and_dump(MemoryTracker(os.path.join(data_path, "memory.json")))
    update_and_dump(DiskTracker(os.path.join(data_path, "disk.json")))
    dump_processes(os.path.join(data_path, "processes.json"))


if __name__ == "__main__":
    plotfree_update()
