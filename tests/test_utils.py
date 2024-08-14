import unittest
from utils.logger import get_logger

class TestLogger(unittest.TestCase):
    def test_get_logger(self):
        logger = get_logger("TestLogger")
        self.assertIsNotNone(logger)

if __name__ == "__main__":
    unittest.main()