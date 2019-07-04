# Dependencies
import re

def error_butler(obj_data):
    '''
        this method validates an email
        this method checks for password strength
        - at least 8 or more characters
        - at least 1 upper case character
        - at least 1 lower case character
        - at least 1 digit
        - at least 1 special character
    '''
    error_tray = dict()
    num = 0
    error_tray['errors'] = num
    email_regex = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    pwd_regex = r'^(?=\S{4,}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])'
    validate_mail = re.match(email_regex, obj_data.email)
    validate_pwd = re.match(pwd_regex, obj_data.password)
    if len(obj_data.username) < 4:
        num += 1
        error_tray['error {}'.format(num)] = 'username must be at least 4 and above characters'
    if (obj_data.username).lower() == (obj_data.name).lower():
        num += 1
        error_tray['error {}'.format(num)] = 'username should not be the same as name'
    if not (obj_data.age).isdigit():
        num += 1
        error_tray['error {}'.format(num)] = 'age must be digits'
    if int(obj_data.age) == 0:
        num += 1
        error_tray['error {}'.format(num)] = 'zero age not allowed'
    if not validate_mail:
        num += 1
        error_tray['error {}'.format(num)] = 'invalid email format'
    if not validate_pwd:
        num += 1
        error_tray['error {}'.format(num)] = 'weak password'
    error_tray['errors'] = num
    return error_tray if num != 0 else False