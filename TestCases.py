# @Author: v sanjay kumar
# @Date: 2024-08-14 11:30:30
# @Last Modified by: v sanjay kumar
# @Last Modified time: 2024-08-14 11:30:30.
# @Title :Python programs of User Registration test cases.

import pytest
from UserRegistration import valid_firstname

def test_firstname():
    assert valid_firstname("Sanjay") == True, "Should be valid"
    assert valid_firstname("Ho") == False, "Should be invalid due to length"
    assert valid_firstname("raju") == False, "Should be invalid due to lowercase first letter"
    assert valid_firstname("Sanj@ay") == False, "Should be invalid due to presence of a special character"
    assert valid_firstname("Sanjay23") == False, "Should be invalid due to presence of a number"

def main():
    test_firstname()
    

if __name__ == "__main__":
   main()
