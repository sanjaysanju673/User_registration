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

def validate_email(mail):
    ''' 
    The function takes the mail frome the user and return the its valid or not

    Parameters-str-mail is user given 

    return bool-True or false 
    '''
    pattern =r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'

    if re.match(pattern, mail):
        return True
    else:
        return False   
    
def validate_mobile_number(mobile):
    ''' 
    The function takes the mobile number frome the user and check the valid or not

    Parameters-str-mobile number is user given 

    return bool-True or false 
    '''
    pattern =r'\+?[0-9]{2}\s[0-9]{10}$'

    if re.match(pattern, mobile):
        return True
    else:
        return False   

def check_password(User_password):
    ''' 
    The function takes the user password and check the it has valid length or not.

    Parameters-str-User Password

    return bool-True or false 
    '''

    pattern =r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_])(?!.*[\W_].*[\W_]).{8,}$'

    if re.match(pattern, User_password):
           return True
    
    else:
        return False 




def main():
    try:
        attempts =0
        while attempts <4 :
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            mail=input("Enter mail address: ")
            number=input("Enter a mobile number")
            user_password=input("Enter user password: ")
            if not valid_firstname(first_name):
                logger.info("First name is not valid. Enter a proper first name.")
                attempts +=1
                continue 
                
            if not validate_lastname(last_name):
                logger.info("Last name is not valid. Enter a proper last name.")
                attempts +=1
                continue 
            if not validate_email(mail):
                logger.info("Email is not valid. Enter a proper mail address.")
                attempts +=1
                continue 
            if not validate_mobile_number(number):
                logger.info("Mail is not valid. Enter a proper mail address.")
                attempts +=1
                continue 
            if not check_password(user_password):
                logger.info("Password is not valid. Enter proper password.")
                attempts +=1
                continue 
            
            logger.info(f"The User name is valid and name is: {first_name } {last_name}")
            logger.info(f'Your email is valid and saved as: {mail}')
            logger.info(f"The mobile number is valid and the number is: {number}")
            logger.info(f'Your password is valid')
            logger.info("Your registration is Succusfully Thanks for registering")
            break  
        if attempts ==4:
                logger.info("Your attempts are over try after some time")

    except Exception as e:
        logger.info('invalid input',e)
         
        
if __name__ == "__main__":
    main()