import unittest
from stream_processing.flink_processing import MaintenanceMapFunction

class TestFlinkProcessing(unittest.TestCase):
    def test_map_function(self):
        map_func = MaintenanceMapFunction()
        result = map_func.map('{"status": "normal", "sensor_1": 40}')
        self.assertIn("Normal operation", result)

if __name__ == "__main__":
    unittest.main()