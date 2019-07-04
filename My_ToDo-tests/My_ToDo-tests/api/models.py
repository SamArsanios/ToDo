'''
	My ToDo v1.0
	models file
	this holds models for;
	1. users
	2. todo lists
	3. todo list items
'''
# model dependencies
import datetime
import uuid

class BaseModel(object):
	'''
		this model generates the following for all objects on instance;
		1. object ids
		2. timestamps 
	'''
	def __init__(self):
		'''
			object constructor
			:param object_id:
			:param date_created:
		'''
		self.object_id = str(uuid.uuid4())
		self.date_created = datetime.datetime.utcnow()
class UserModel(BaseModel):
	'''
		this is the user model
		holds methods for;
		1. user object constructor
		2. displaying user object details
	'''
	def __init__(self, json_dict):
		'''
			object constructor
			:param names:
			:param email:
			:param password:
		'''
		BaseModel.__init__(self)
		self.name = json_dict['name']
		self.username = json_dict['username']
		self.age = str(json_dict['age'])
		self.email = json_dict['email']
		self.password = json_dict['password']
		self.gender = json_dict['gender']
	def __repr__(self):
		'''
			default user object display
		'''
		return "<{}: {}>".format(self.name, self.email)		
class ToDoListModel(BaseModel):
	'''
		this is the todo list model
		holds methods for;
		1. todo list object constructor
		2. displaying todo list object details
	'''
	def __init__(self, input_tuple):
		'''
			object constructor
			:param owner_email:
			:param title:
			:param description:
		'''
		BaseModel.__init__(self)
		self.owner_email = input_tuple[0]
		self.title = input_tuple[1]
		self.description = input_tuple[2]
	def display_todo_list(self):
		display_todo = dict()
		display_todo['title'] = self.title
		display_todo['description'] = self.description
	def __repr__(self):
		return "<{}: {}>".format(self.title, self.date_created)
class ToDoItemModel(BaseModel):
	'''
		this model holds methods for;
		1. creating a todo item object
		2. fetching and displaying a todo item object
	'''
	def __init__(self):
		BaseModel.__init__(self)
		self.todo_list_id = str() # acts as a foreign key
		self.item = str()
		self.status = False
	def display_item(self):
		item_display = dict()
		item_display['item name'] = self.item
		item_display['status'] = 'done' if self.status == True else 'pending'
		return item_display
	def __repr__(self):
		return "{}: {}".format(self.item, self.date_created)
