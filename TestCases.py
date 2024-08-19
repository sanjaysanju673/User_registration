'''
@Author: v sanjay kumar
@Date: 2024-08-14 11:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-08-14 11:30:30.
@Title :Python programs of User Registration test cases.

'''


import unittest
from UserRegistration import valid_firstname

class TestNameValidation(unittest.TestCase):
    def test_firstname(self):
        self.assertTrue(valid_firstname("Sanjay"), "Should be valid")
        self.assertTrue(valid_firstname("Rahul"), "Should be valid")
        self.assertFalse(valid_firstname("Ho"), "Should be invalid due to length")
        self.assertFalse(valid_firstname("fi"), "Should be invalid due to length")
        self.assertFalse(valid_firstname("raju"), "Should be invalid due to lowercase first letter")
        self.assertFalse(valid_firstname("ramyasree"), "Should be invalid due to lowercase first letter")
        self.assertFalse(valid_firstname("Sanj@ay"), "Should be invalid due to presence of a special character")
        self.assertFalse(valid_firstname("Sanj!ay"), "Should be invalid due to presence of a special character")
        self.assertFalse(valid_firstname("Sanjay23"), "Should be invalid due to presence of a number")
        self.assertFalse(valid_firstname("Girish456"), "Should be invalid due to presence of a number")

if __name__ == "__main__":
    unittest.main()
