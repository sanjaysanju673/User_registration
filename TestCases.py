'''
@Author: v sanjay kumar
@Date: 2024-08-19 11:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-08-19 11:30:30.
@Title :Python programs of User Registration test cases.

'''


import unittest

from UserRegistration import valid_firstname,validate_lastname,validate_email
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


    def test_valid_last_name(self):
        """
        Description:
            Tests the validation function for last names.

        Parameter:
            self: Instance of the class.

        Return:
            None
        """

        self.assertTrue(validate_lastname("Naik"),"Should be valid")
        self.assertTrue(validate_lastname("Nekar"),"Should be valid")
        self.assertFalse(validate_lastname("Ho"), "Should be invalid due to length")
        self.assertFalse(validate_lastname("Mi"), "Should be invalid due to length")
        self.assertFalse(validate_lastname("naik"),"Should be invalid due to lowercase first letter")
        self.assertFalse(validate_lastname("nekar"),"Should be invalid due to lowercase first letter")
        self.assertFalse(validate_lastname("nai@k"), "Should be invalid due to  presence of a special character")
        self.assertFalse(validate_lastname("nai!k"),  "Should be invalid due to  presence of a special character")
        self.assertFalse(validate_lastname("Naik123"), "Should be invalid due to  presence of a Number")
        self.assertFalse(validate_lastname("Naik456"), "Should be invalid due to  presence of a Number")
    
    def test_valid_email(self):
    
        """
        Description:
            Tests the validation function for emails.

        Parameter:
            self: Instance of the class.

        Return:
            None
        """

        self.assertTrue(validate_email("abc.xyz@bl.co.in"), "Should be valid")
        self.assertTrue(validate_email("sanjay@bl.co"), "Should be valid")
        self.assertFalse(validate_email("sanjay@blco"), "Should be invalid due to missing dot before TLD")
        self.assertFalse(validate_email("sanjay@bl.co.in."), "Should be invalid due to trailing dot")
        self.assertFalse(validate_email("sanjay@gmailcom"), "Should be invalid due to missing dot in domain")
        self.assertFalse(validate_email("@bl.co"), "Should be invalid due to missing user part")
        self.assertFalse(validate_email("sanjay@.com"), "Should be invalid due to missing domain part")
        self.assertFalse(validate_email("sanjay@domain.c"), "Should be invalid due to TLD being too short")
        self.assertFalse(validate_email("sanjay@domain.toolongtld"), "Should be invalid due to TLD being too long")
        self.assertFalse(validate_email("sanjaygamil.com"), "Should be invalid due to missing @ symbol")



if __name__ == "__main__":
    unittest.main()
