import os
import unittest

from .memory_tracker import MemoryTracker


class TestMemoryTracker(unittest.TestCase):
    def test_dump_empty_file(self):
        f = os.tmpnam()
        writer = MemoryTracker(f)
        writer.dump()
        reader = MemoryTracker(f)
        self.assertEqual(reader.data_points, [])

    def test_dump_single_point_file(self):
        f = os.tmpnam()
        writer = MemoryTracker(f)
        writer.add_data_point()
        writer.dump()
        reader = MemoryTracker(f)
        self.assertEqual(len(reader.data_points), 1)

    def test_dump_limited_data_points(self):
        f = os.tmpnam()
        writer = MemoryTracker(f)

        for i in range(0, 10):
            writer.add_data_point()
        writer.dump(4)

        reader = MemoryTracker(f)
        self.assertEqual(len(reader.data_points), 4)
