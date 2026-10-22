import unittest
from app import SimpleHandler

class TestDevOpsApp(unittest.TestCase):
    def test_handler_exists(self):
        """Verify our web handler is defined and ready."""
        self.assertTrue(hasattr(SimpleHandler, "do_GET"))

if __name__ == '__main__':
    unittest.main()
