import json
from psutil import process_iter

from .util import bytes_to_megabytes


def processes_and_memory_usage_in_bytes():
    grouped_processes = {}

    # Loop over the processes, and build up a list of their memory
    # usages, in bytes
    for proc in process_iter():
        if proc.name not in grouped_processes:
            grouped_processes[proc.name] = []
            rss = proc.get_memory_info().rss
            grouped_processes[proc.name].append(rss)

    # Sum up memory usage for each process, grouped by process name
    return {k: sum(v)
            for (k, v) in grouped_processes.items()}


def dump_processes(filename):
    raw_data = processes_and_memory_usage_in_bytes()
    data = [{"label": k, "data": bytes_to_megabytes(v)}
            for (k, v) in raw_data.items()]

    with open(filename, "w") as f:
        f.write(json.dumps(data))
