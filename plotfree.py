from memory_tracker import MemoryTracker


m = MemoryTracker("public_html/data/memory.json")
m.add_data_point()
m.dump()
