'''
    My ToDo v1.0
    accounts file
    holds sign in and login methods for the application
'''
from flask import request, Response
from flask_restful import Resource
from passlib.hash import pbkdf2_sha256
from .models import UserModel
from .db_model import DatabaseModel
from .error_handler import error_butler

# Database object instance
DB = DatabaseModel()
current_user = list()
class Home(Resource):
    def get(self):
        return "Welcome to My_ToDo", 200
        
class User(Resource):
    '''
        sign up method does the following;
        1. checking for email format
        2. checking if email already in use
        3. checking for password strength;
            - hint: password_requirements variable in validation file
    '''
    def get(self):
        user_list = list()
        for user in DB.user_tb:
            user_list.append(user.email)
        return user_list if user_list else "No users available", 200
    def post(self):
        json_data = request.get_json()
        require_fields = ['name', 'username', 'age', 'email', 'password', 'gender']
        for keys in json_data.keys():
            if keys not in require_fields:
                return {"error": "json field missing"}, 400
        for values in json_data.values():
            if values == "":
                return {"error": "empty fields detected"}, 400
        new_user = UserModel(json_data)
        if error_butler(new_user):
            return error_butler(new_user), 400
        if DB.dup_check_user(new_user, 'user'):
            return {"error": "email already in use"}, 400
        hashed_password = pbkdf2_sha256.hash(new_user.password)
        new_user.password = hashed_password
        DB.save_user_object(new_user, 'user')
        return {"message": "registration successful"}, 201
    
class ToDoList(Resource):
    def get(self):
        todo_listing = list()
        for todo in DB.todo_tb:
            todo_listing.append(todo.display_todo_list())
        return todo_listing
    def post(self):
        json_data = request.get_json()

    # new_user = UserModel(input_tuple)
    # if DB.object_dup(new_user, 'user'):
    #     return False
    # if not DB.save_object(new_user, 'user'):
    #     return False
    # current_user.append(new_user)
    # return True

# def login_form(input_tuple):
#     '''
#         login method authenticates a user
#     '''
#     hashed_password = pbkdf2_sha256.hash(str(input_tuple[1]))
#     email = str(input_tuple[0])
#     pwd = hashed_password
#     if not DB.auth(email, pwd):
#         return False
#     current_user.append(DB.auth(email, pwd))
#     return DB.auth(email, pwd)

# def user_select_option(user_option):    
#     current_user.clear()
#     if user_option == 1:
#         signup_dict = dict()
#         print("----------- SIGN UP -----------")
#         name = input("enter your names: ")
#         email = input("enter your email: ")
#         pwd = input("enter your password: ")
#         confirm_pwd = input("confirm your password: ")
#         signup_dict['name'] = name
#         signup_dict['email'] = email
#         signup_dict['pwd'] = pwd
#         signup_dict['confirm_pwd'] = confirm_pwd
#         input_tuple = (name, email, pwd, confirm_pwd)
#         if error_butler(signup_dict):
#             print("----------- OUTPUT RESULT -----------")
#             print(error_butler(signup_dict))
#             print("-------------------------------------")            
#             return "error"
#         else:
#             if not sign_up_form(input_tuple):
#                 print("----------- OUTPUT RESULT -----------")
#                 print({"error": "email already taken"})
#                 print("-------------------------------------")
#                 return "error"
#             else:          
#                 print("----------- OUTPUT RESULT -----------")
#                 print("Sign up successful")
#                 print("Hello, {}!".format(name))
#                 print("-------------------------------------")
#     if user_option == 2:
#         login_dict = dict()
#         print("----------- LOGIN -----------")
#         email = input("enter your email: ")
#         pwd = input("enter your password: ")
#         login_dict['email'] = email
#         login_dict['pwd'] = pwd
#         input_tuple = (email, pwd)        
#         if [field for field in input_tuple if field == ""]:
#             print("----------- OUTPUT RESULT -----------")
#             print({"error": "missing fields"})
#             print("-------------------------------------")
#             return "error"
#         else:
#             if not login_form(input_tuple):
#                 print("----------- OUTPUT RESULT -----------")
#                 print({"error": "invalid logins"})
#                 print("-------------------------------------")
#                 return "error"
#             else:          
#                 print("----------- OUTPUT RESULT -----------")
#                 print("Login successful")
#                 print("Hello, {}!".format(login_form(input_tuple).names))
#                 print("-------------------------------------")
