'''
	My ToDo v1.0
	database model file
	this model holds all interactions with the database
	note: this is a non-persistent database
'''
from .models import BaseModel

class DatabaseModel(BaseModel):
    '''
        this is the database model that holds;
        1. the user table
        2. the todo list table
        3. the todo list item table
        this model also holds methods for;
        1. adding an object to a table in the database
        2. fetching a specific object from a corresponding table
        3. updating a specific object from a corresponding table
        4. deleting a specific object from a corresponding table
        5. cleaning out data stored in a specific table
    '''
    def __init__(self):
        '''
                object constructor
                :param user_tb:
                :param user_tb:
                :param user_tb:
        '''
        BaseModel.__init__(self)
        self.user_tb = list()
        self.todo_tb = list()
        self.todo_items_tb = list()
        self.user_object = str()
        self.todo_object = str()
        self.item_object = str()

    def save_user_object(self, object_data):
        '''
            this method saves a user object to the user table
        '''
        self.user_tb.append(object_data)
        return True
    def save_todo_object(self, object_data):
        '''
            this method saves a todo object to the user table
        '''
        self.todo_tb.append(object_data)
        return True 
    def save_item_object(self, object_data):
        '''
            this method saves a todo item object to the user table
        '''
        self.todo_items_tb.append(object_data)
        return True

    def dup_check_user(self, object_data):
        '''
            this method checks for a duplicate of a user
        '''
        for user_obj in self.user_tb:
            return True if object_data.email == user_obj.email else False
    def dup_check_todo(self, object_data):
        '''
            this method checks for a duplicate of a todo list
        '''
        for todo_obj in self.todo_tb:
            title_match = todo_obj.title == object_data.title
            email_match = todo_obj.owner_email == object_data.owner_email
            if title_match and email_match:
                return True
    def dup_check_item(self, object_data):
        '''
            this method checks for a duplicate of an item
        '''
        for item_obj in self.todo_items_tb:
            if object_data.item == item_obj.item:
                return True
        return False
        
    def auth(self, email, pwd):
        '''
            this method authenticates a user logging in
        '''
        get_user = [user for user in self.user_tb if user.email == email]
        return get_user[0] if get_user else False
    def fetch_user_object(self, object_id):
        '''
            this method fetches a user object
        '''
        user_obj = [
            user_obj for user_obj in self.user_tb if user_obj.object_id == object_id]
        return user_obj[0] if user_obj else False
    def fetch_todo_object(self, object_id):
        '''
            this method fetches a todo object
        '''
        todo_obj = [
            todo_obj for todo_obj in self.todo_tb if todo_obj.object_id == object_id]
        return todo_obj[0] if todo_obj else False
    def fetch_item_object(self, object_id):
        '''
            this method fetches an item object
        '''
        item_obj = [
            item_obj for item_obj in self.todo_items_tb if item_obj.object_id == object_id]
        return item_obj[0] if item_obj else False
    def fetch_all_users(self):
        pass
    def fetch_all_todo(self):
        return self.todo_tb
    def fetch_all_item(self):
        pass

    def update_user_object(self, object_data):
        '''
            this method updates a user object
        '''
        for user_obj in self.user_tb:
            if user_obj.object_id == object_data.object_id:
                index = self.user_tb.index(user_obj[0])
                self.user_tb[index] = object_data
                return True
    def update_todo_object(self, object_data):
        '''
            this method updates a todo object
        '''
        for todo_obj in self.todo_tb:
            if todo_obj.object_id == object_data.object_id:
                index = self.todo_tb.index(todo_obj[0])
                self.todo_tb[index] = object_data
                return True
    def update_item_object(self, object_data):
        '''
            this method updates an item object
        '''
        for item_obj in self.todo_items_tb:
            if item_obj.object_id == object_data.object_id:
                index = self.todo_items_tb.index(item_obj[0])
                self.todo_items_tb[index] = object_data
                return True

    def delete_user_object(self, object_data):
        '''
            this method deletes a user object from the user table
        '''
        self.user_tb.remove(object_data)
        return True
    def delete_todo_object(self, object_data):
        '''
            this method deletes a todo object from the todo table
        '''
        self.todo_tb.remove(object_data)
        return True
    def delete_items_object(self, object_data):
        '''
            this method deletes a item object from the item table
        '''
        self.todo_items_tb.remove(object_data)
        return True

    def clear_user_table(self):
        '''
            this method cleans out the user table
        '''
        self.user_tb.clear()
        return True
    def clear_todo_table(self):
        '''
            this method cleans out the todo list table
        '''
        self.todo_tb.clear()
        return True
    def clear_item_table(self):
        '''
            this method cleans out the todo items table
        '''
        self.todo_items_tb.clear()
        return True
