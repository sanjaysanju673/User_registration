
import pytest
from UserRegistration import valid_firstname, validate_lastname, validate_email, validate_mobile_number

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
    assert validate_lastname("naik") is False, "Should be invalid due to lowercase first letter"
    assert validate_lastname("nekar") is False, "Should be invalid due to lowercase first letter"
  
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
    assert validate_email("@bl.co") is False, "Should be invalid due to missing user part"
    assert validate_email("sanjay@.com") is False, "Should be invalid due to missing domain part"
    assert validate_email("sanjay@domain.c") is False, "Should be invalid due to TLD being too short"
    assert validate_email("sanjay@domain.toolongtld") is False, "Should be invalid due to TLD being too long"

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
    assert validate_mobile_number("+44 1234567890") is True, "Should be valid"
    assert validate_mobile_number("918431852455") is False, "Should be invalid due to missing space"
    assert validate_mobile_number("91 84318524") is False, "Should be invalid due to insufficient digits"

if __name__=="__main__":
    pytest.main()