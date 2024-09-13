'''
@Author: v sanjay kumar
@Date: 2024-08-19 11:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-08-19 11:30:30.
@Title :Python programs of User Registration.

'''

import pytest
from UserRegistration import valid_firstname, validate_lastname

def test_firstname():
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
    assert validate_lastname("Ho") is False, "Should be invalid due to length"
    assert validate_lastname("vadde") is False, "Should be invalid due to lowercase first letter"
    assert validate_lastname("ra@m") is False, "Should be invalid due to presence of a special character"
    assert validate_lastname("kumar123") is False, "Should be invalid due to presence of a number"
