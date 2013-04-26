from memory_tracker import MemoryTracker


m = MemoryTracker("data.json")
m.add_data_point()
m.dump()
