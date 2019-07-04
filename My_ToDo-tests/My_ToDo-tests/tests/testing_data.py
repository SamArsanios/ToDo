
clean_user = dict()
clean_user['name'] =  "John"
clean_user['username'] = "zeus"
clean_user['age'] = 10
clean_user['email'] = "zack@mail.com"
clean_user['password'] = "aS@asfdasdf333"
clean_user['gender'] = "M"

name_username_error = clean_user
name_username_error['username'] = "john"

username_error = clean_user
username_error['username'] = 'tom'

email_error = clean_user
email_error['email'] = 'asdfasdfasdf'

password_error = clean_user
password_error['password'] = 'asdf34fasdf'

age_error = clean_user
age_error['age'] = 'asdf'

zero_age_error = clean_user
zero_age_error['age'] = 0