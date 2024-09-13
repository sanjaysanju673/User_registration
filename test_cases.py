'''
@Author: v sanjay kumar
@Date: 2024-08-19 12:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-08-19 12:30:30.
@Title :Python programs of User Registration test cases.

'''


# test_user_registration.py

import pytest
from UserRegistration import (valid_firstname, validate_lastname, validate_email, validate_mobile_number, check_password)

def test_firstname():
    """
    Description:
        Tests the validation function for first names.

    Parameter:
        None

    Return:
        None
    """
    assert valid_firstname("Sanjay") is True, "Should be valid"
    assert valid_firstname("Ho") is False, "Should be invalid due to length"
    assert valid_firstname("raju") is False, "Should be invalid due to lowercase first letter"
    assert valid_firstname("Sanj@ay") is False, "Should be invalid due to presence of a special character"
    assert valid_firstname("Sanjay23") is False, "Should be invalid due to presence of a number"

def test_valid_last_name():
    """
    Description:
        Tests the validation function for last names.

    Parameter:
        None

    Return:
        None
    """
    assert validate_lastname("Vadde") is True, "Should be valid"
    assert validate_lastname("Dandu") is True, "Should be valid"
    assert validate_lastname("Mi") is False, "Should be invalid due to length"
    assert validate_lastname("vadde") is False, "Should be invalid due to lowercase first letter"
    assert validate_lastname("ram@s") is False, "Should be invalid due to presence of a special character"
    assert validate_lastname("raja123") is False, "Should be invalid due to presence of a number"

def test_valid_email():
    """
    Description:
        Tests the validation function for emails.

    Parameter:
        None

    Return:
        None
    """
    assert validate_email('abc@yahoo.com') is True
    assert validate_email('abc-100@yahoo.com') is True
    assert validate_email('abc.100@yahoo.com') is True
    assert validate_email('abc111@abc.com') is True
    assert validate_email('abc-100@abc.net') is True
    assert validate_email('abc.100@abc.com.au') is True
    assert validate_email('abc@1.com') is True
    assert validate_email('abc@gmail.com.com') is True
    assert validate_email('abc+100@gmail.com') is True

    assert validate_email('abc') is False
    assert validate_email('abc@.com.my') is False
    assert validate_email('abc123@gmail.a') is False
    assert validate_email('abc123@.com') is False
    assert validate_email('abc123@.com.com') is False
    assert validate_email('abc()*@gmail.com') is False
    assert validate_email('.abc@abc.com') is False
    assert validate_email('abc@%*.com') is False
    assert validate_email('abc..2002@gmail.com') is False
    assert validate_email('abc@abc@gmail.com') is False
    assert validate_email('abc@gmail.com.1a') is False
    assert validate_email('abc@gmail.com.aa.au') is False

def test_valid_mobile_number():
    """
    Description:
        Tests the validation function for mobile numbers.

    Parameter:
        None

    Return:
        None
    """
    assert validate_mobile_number("91 8431852455") is True
    assert validate_mobile_number("91 1234567890") is True
    assert validate_mobile_number("+44 1234567890") is True
    assert validate_mobile_number("918431852455") is False, "Should be invalid due to missing space"
    assert validate_mobile_number("91 84318524") is False, "Should be invalid due to insufficient digits"
    assert validate_mobile_number("91 99198198012") is False, "Should be invalid due to excessive digits"
    assert validate_mobile_number("91-9919453241") is False, "Should be invalid due to incorrect separator"

def test_validate_user_password():
    """
    Description:
        Tests the validation function for user passwords.

    Parameter:
        None

    Return:
        None
    """
    assert check_password("Vadde@341") is True, "Should be valid"
    assert check_password("Dandu@238") is True, "Should be valid"
    assert check_password("dandu") is False, "Should be invalid due to lowercase and missing numeric number"
    assert check_password("Mi") is False, "Should be invalid due to length"
    assert check_password("Minmm234") is False, "Should be invalid due to absence of a special character"

if __name__=="__main__":
    pytest.main()