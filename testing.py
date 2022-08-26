import unittest
from utils import visitor_counter


class StringChecker(unittest.TestCase):
    def test_string_datatype(self):
        test_string = visitor_counter()
        self.assertTrue(isinstance(test_string, str))

if __name__ == "__main__":
    unittest.main()