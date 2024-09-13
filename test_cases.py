'''
@Author: v sanjay kumar
@Date: 2024-08-19 11:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-08-19 11:30:30.
@Title :Python programs of test cases
'''
import pytest
from UserRegistration import valid_firstname, validate_lastname, validate_email

def test_firstname():
    assert valid_firstname("Sanjay") is True, "Should be valid"
    assert valid_firstname("Rahul") is True, "Should be valid"
    assert valid_firstname("Ho") is False, "Should be invalid due to length"
    assert valid_firstname("fi") is False, "Should be invalid due to length"
    assert valid_firstname("raju") is False, "Should be invalid due to lowercase first letter"
    assert valid_firstname("ramyasree") is False, "Should be invalid due to lowercase first letter"

def test_valid_last_name():
    """
    Description:
        Tests the validation function for last names.

    Parameter:
        None

    Return:
        None
    """
    assert validate_lastname("Naik") is True, "Should be valid"
    assert validate_lastname("Nekar") is True, "Should be valid"
    assert validate_lastname("Ho") is False, "Should be invalid due to length"
    assert validate_lastname("Mi") is False, "Should be invalid due to length"
    assert validate_lastname("nai@k") is False, "Should be invalid due to presence of a special character"

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
    assert validate_email("sanjay@bl.co.in.") is False, "Should be invalid due to trailing dot"
    assert validate_email("sanjay@gmailcom") is False, "Should be invalid due to missing dot in domain"
    assert validate_email("@bl.co") is False, "Should be invalid due to missing user part"
