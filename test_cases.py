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
    assert valid_firstname("Rahul") is True, "Should be valid"
    assert valid_firstname("Ho") is False, "Should be invalid due to length"
    assert valid_firstname("fi") is False, "Should be invalid due to length"
    assert valid_firstname("raju") is False, "Should be invalid due to lowercase first letter"
    assert valid_firstname("Sanj@ay") is False, "Should be invalid due to presence of a special character"

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
    assert validate_email("abc.xyz@bl.co.in") is True, "Should be valid"
    assert validate_email("sanjay@bl.co") is True, "Should be valid"
    assert validate_email("sanjay@blco") is False, "Should be invalid due to missing dot before TLD"
    assert validate_email("sanjay@gmailcom") is False, "Should be invalid due to missing dot in domain"
    assert validate_email("@bl.co") is False, "Should be invalid due to missing user part"
    assert validate_email("sanjay@domain.c") is False, "Should be invalid due to TLD being too short"

def test_valid_mobile_number():
    """
    Description:
        Tests the validation function for mobile numbers.

    Parameter:
        None

    Return:
        None
    """
    assert validate_mobile_number("91 8431852455") is True, "Should be valid"
    assert validate_mobile_number("91 1234567890") is True, "Should be valid"
    assert validate_mobile_number("91 9919819801") is True, "Should be valid"
    assert validate_mobile_number("+44 1234567890") is True, "Should be valid"
    assert validate_mobile_number("918431852455") is False, "Should be invalid due to missing space"
    assert validate_mobile_number("91 84318524") is False, "Should be invalid due to insufficient digits"
    

def test_validate_user_password():
    """
    Description:
        Tests the validation function for user passwords.

    Parameter:
        None

    Return:
        None
    """
    assert check_password("Vadde341") is True, "Should be valid"
    assert check_password("Dandu238") is True, "Should be valid"
    assert check_password("dandu123") is False, "Should be invalid due to lowercase"
    assert check_password("Mi") is False, "Should be invalid due to length"


if __name__=="__main__":
    pytest.main()