'''
@Author: v sanjay kumar
@Date: 2024-08-19 12:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-08-19 12:30:30.
@Title :Python programs of User Registration test cases.

'''


import unittest

from UserRegistration import (valid_firstname,validate_lastname,validate_email,validate_mobile_number,check_password)
class TestNameValidation(unittest.TestCase):
    def test_firstname(self):
        """
        Description:
            Tests the validation function for last names.

        Parameter:
            self: Instance of the class.

        Return:
            None
        """
        self.assertTrue(valid_firstname("Sanjay"), "Should be valid")
        self.assertFalse(valid_firstname("Ho"), "Should be invalid due to length")
        self.assertFalse(valid_firstname("raju"), "Should be invalid due to lowercase first letter")
        self.assertFalse(valid_firstname("Sanj@ay"), "Should be invalid due to presence of a special character")
        self.assertFalse(valid_firstname("Sanjay23"), "Should be invalid due to presence of a number")



    def test_valid_last_name(self):
        """
        Description:
            Tests the validation function for last names.

        Parameter:
            self: Instance of the class.

        Return:
            None
        """

        self.assertTrue(validate_lastname("Vadde"),"Should be valid")
        self.assertTrue(validate_lastname("Dandu"),"Should be valid")
        self.assertFalse(validate_lastname("Mi"), "Should be invalid due to length")
        self.assertFalse(validate_lastname("vadde"),"Should be invalid due to lowercase first letter")
        self.assertFalse(validate_lastname("ram@s"), "Should be invalid due to  presence of a special character")
        self.assertFalse(validate_lastname("raja123"), "Should be invalid due to  presence of a Number")

    
    def test_valid_email(self):
    
        """
        Description:
            Tests the validation function for emails.

        Parameter:
            self: Instance of the class.

        Return:
            None
        """

        self.assertTrue(validate_email('abc@yahoo.com'))
        self.assertTrue(validate_email('abc-100@yahoo.com'))
        self.assertTrue(validate_email('abc.100@yahoo.com'))
        self.assertTrue(validate_email('abc111@abc.com'))
        self.assertTrue(validate_email('abc-100@abc.net'))
        self.assertTrue(validate_email('abc.100@abc.com.au'))
        self.assertTrue(validate_email('abc@1.com'))
        self.assertTrue(validate_email('abc@gmail.com.com'))
        self.assertTrue(validate_email('abc+100@gmail.com'))

        self.assertFalse(validate_email('abc'))
        self.assertFalse(validate_email('abc@.com.my'))
        self.assertFalse(validate_email('abc123@gmail.a'))
        self.assertFalse(validate_email('abc123@.com'))
        self.assertFalse(validate_email('abc123@.com.com'))
        self.assertFalse(validate_email('abc()*@gmail.com'))
        self.assertFalse(validate_email('.abc@abc.com'))
        self.assertFalse(validate_email('abc@%*.com'))
        self.assertFalse(validate_email('abc..2002@gmail.com'))
        self.assertFalse(validate_email('abc@abc@gmail.com'))
        self.assertFalse(validate_email('abc@gmail.com.1a'))
        self.assertFalse(validate_email('abc@gmail.com.aa.au'))
        


    def test_valid_mobile_number(self):
    
        """
        Description:
            Tests the validation function for mobile number.

        Parameter:
            self: Instance of the class.

        Return:
            None
        """    
        self.assertTrue(validate_mobile_number("91 8431852455"), "Should be valid")
        self.assertTrue(validate_mobile_number("91 1234567890"), "Should be valid")
        self.assertFalse(validate_mobile_number("918431852455"), "Should be invalid due to missing space")
        self.assertFalse(validate_mobile_number("91 84318524"), "Should be invalid due to insufficient digits")
        self.assertFalse(validate_mobile_number("91 99198198012"), "Should be invalid due to excessive digits")
        self.assertFalse(validate_mobile_number("91-9919453241"), "Should be invalid due to incorrect separator")


    def test_validate_user_password(self):
        """
        Description:
            Tests the validation function for user password

        Parameter:
            self: Instance of the class.

        Return:
            None
        """

        self.assertTrue(check_password("Vadde@341"),"Should be valid")
        self.assertTrue(check_password("Dandu@238"),"Should be valid")
        self.assertFalse(check_password("dandu"),'shoud be invalid due to lowercase and does\'t have numeric number')
        self.assertFalse(check_password("Mi"), "Should be invalid due to length")
        self.assertFalse(check_password("Minmm234"), "Should be invalid due to absent of the special charecter")




if __name__ == "__main__":
    unittest.main()
