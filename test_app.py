import unittest
from app import SimpleHandler

class TestDevOpsApp(unittest.TestCase):
    def test_handler_exists(self):
        # This will FAIL because 'broken_function' does not exist in our app!
        self.assertTrue(hasattr(SimpleHandler, "broken_function"))

if __name__ == '__main__':
    unittest.main()
