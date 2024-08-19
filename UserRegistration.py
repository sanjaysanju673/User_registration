'''
@Author: v sanjay kumar
@Date: 2024-08-19 11:30:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-08-19 11:30:30.
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
    
def validate_lastname(last_name):
    ''' 
    The function takes the last name frome the user and return the its valid or not

    Parameters-str-last name of the User 

    return bool-True or false 
    '''
    pattern =r'^[A-Z][a-zA-Z]{2,}$'

    if re.match(pattern, last_name) :
        return True
    else:
        return False

def main():
    while True:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
    
        if not valid_firstname(first_name):
            logger.info("First name is not valid. Enter a proper first name.")
            continue 
        
        if not validate_lastname(last_name):
            logger.info("Last name is not valid. Enter a proper last name.")
            continue 
        
        logger.info("The User name is valid")
        break  
             
        
    
if __name__ == "__main__":
    main()