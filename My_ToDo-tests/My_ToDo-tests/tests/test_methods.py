'''
    My ToDo v1.0
    tests file
    holds all tests for all methods in the application
'''
import unittest
from flask import json
from api.app import APP
from api.db_model import DatabaseModel
from api.models import UserModel
from testing_data import (clean_user, name_username_error, username_error, email_error, password_error, age_error, zero_age_error)

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.client = APP.test_client(self)
    def test_user_get(self):
        response = self.client.get('/sign_up', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    def test_user_signup_pass(self):
        # response = self.client.post('/sign_up', data = json.dumps(clean_user), content_type = 'application/json')
        # self.assertEqual(response.status_code, 201)
        pass
    def test_name_username_error(self):
        response = self.client.post('/sign_up', data = json.dumps(name_username_error), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
    def test_username_error(self):
        response = self.client.post('/sign_up', data = json.dumps(username_error), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
    def test_email_error(self):
        response = self.client.post('/sign_up', data = json.dumps(email_error), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
    def test_password_error(self):
        response = self.client.post('/sign_up', data = json.dumps(password_error), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)    
    def test_age_error(self):
        response = self.client.post('/sign_up', data = json.dumps(age_error), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
    def test_zero_age_error(self):
        response = self.client.post('/sign_up', data = json.dumps(zero_age_error), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
    def test_login_pass(self):
        pass
    def test_login_fail(self):
        pass
    def test_create_task_pass(self):
        pass
    def test_create_task_fail(self):
        pass
    def test_delete_task_pass(self):
        pass
    def test_delete_task_fail(self):
        pass
    def test_mark_as_finished_pass(self):
        pass
    def test_mark_as_finished_fail(self):
        pass

if __name__ == "__main__":
    unittest.main()
