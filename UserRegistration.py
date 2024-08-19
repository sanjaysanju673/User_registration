'''
@Author: v sanjay kumar
@Date: 2024-08-14 11:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-08-14 11:30:30.
@Title :Python programs of User Registration.

'''

import re
import mylogging as log

logger=log.logger_init("UserRegistration.py")


def valid_firstname(first_name):
    ''' 
    The function takes the first name frome the user and return the its valid or not

    Parameters-str-First name of the User 

    return bool-True or false of the first name
    '''
    pattern =r'^[A-Z][a-zA-Z]{2,}$'

    
    if re.match(pattern, first_name) :
        return True
    else:
        return False

def main():
    first_name=input("Enter a first name: ")

    if valid_firstname(first_name):
        logger.info("The User  first name is valid")
    
    else:
        logger.info("first name is not valid")
    
    


if __name__ == "__main__":
    main()