import os.path
import shutil
import tempfile
import unittest
import uuid

from .memory_tracker import MemoryTracker


class DummyTracker(MemoryTracker):
    def add_data_point(self):
        self.data_points.append((1, 2))


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.dir)


class TestDummyTracker(BaseTest):
    def test_dump_empty_file(self):
        f = os.path.join(self.dir, str(uuid.uuid4()))
        writer = DummyTracker(f)
        writer.dump()
        reader = DummyTracker(f)
        self.assertEqual(reader.data_points, [])

    def test_dump_single_point_file(self):
        f = os.path.join(self.dir, str(uuid.uuid4()))
        writer = DummyTracker(f)
        writer.add_data_point()
        writer.dump()
        reader = DummyTracker(f)
        self.assertEqual(len(reader.data_points), 1)
        self.assertEqual(reader.data_points[0], [1, 2])

    def test_dump_limited_data_points(self):
        f = os.path.join(self.dir, str(uuid.uuid4()))
        writer = DummyTracker(f)

        for i in range(0, 10):
            writer.add_data_point()
        writer.dump(4)

        reader = DummyTracker(f)
        self.assertEqual(len(reader.data_points), 4)


class TestRealTracker(BaseTest):
    def test_dump_single_point_file(self):
        f = os.path.join(self.dir, str(uuid.uuid4()))
        writer = MemoryTracker(f)
        writer.add_data_point()
        writer.dump()
        reader = MemoryTracker(f)
        self.assertEqual(len(reader.data_points), 1)
