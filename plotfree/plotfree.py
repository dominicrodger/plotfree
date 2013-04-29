from memory_tracker import MemoryTracker


m = MemoryTracker("public_html/data/memory.json")
m.add_data_point()

# Only dump the latest 1440 points - intended for half-hourly stats
# for a month (2 * 24 * 30)
m.dump(1440)
