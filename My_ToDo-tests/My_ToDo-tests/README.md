![](https://atamazack.github.io/My_ToDo/static/logo.jpg)
## My_ToDo
#### About
This is an application that helps users create different to-do lists to better track their productivity. Every ToDo list created has items to be completed off the list.

#### Application test badges
[![Build Status](https://travis-ci.org/AtamaZack/My_ToDo.svg?branch=tests)](https://travis-ci.org/AtamaZack/My_ToDo) [![Maintainability](https://api.codeclimate.com/v1/badges/3b3b693b1f10c4d24d22/maintainability)](https://codeclimate.com/github/AtamaZack/My_ToDo/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/3b3b693b1f10c4d24d22/test_coverage)](https://codeclimate.com/github/AtamaZack/My_ToDo/test_coverage) [![Coverage Status](https://coveralls.io/repos/github/AtamaZack/My_ToDo/badge.svg?branch=tests)](https://coveralls.io/github/AtamaZack/My_ToDo?branch=tests)

#### Development setup
- Clone the project using this link `https://github.com/AtamaZack/My_ToDo.git`

#### Frontend/UI Design
##### Page layouts (gh-pages demo)
| Feature name | Description | gh-pages URLs |
| :---------------- |:---------------| :---------------|
| Landing page | Serves as the first page to be opened by the web server | [landing page](https://atamazack.github.io/My_ToDo/) |
| Signup | Page where a new user can registers to the platform | [sign up](https://atamazack.github.io/My_ToDo/templates/sign_up.html) |
| Login | Page where a user logs into the platform | [login](https://atamazack.github.io/My_ToDo/templates/login.html) |
| Dashboard | This is the main user account page | [dashboard](https://atamazack.github.io/My_ToDo/templates/dashboard.html) |
| Create new ToDo | The page where a new ToDo list is create | [new todo](https://atamazack.github.io/My_ToDo/templates/create_todo.html) |
| Add item | The page where a new item is added to a ToDo list | [add item](https://atamazack.github.io/My_ToDo/templates/add_items.html) |
| All ToDoes | The page that shows all ToDo lists ever created by the user | [all todoes](https://atamazack.github.io/My_ToDo/templates/all_todoes.html) |

#### Backend (Flask Restful API)
The backend is a flask restful web api by `python app.py` command in terminal.
##### Application backend features
- Signing up to the application by providing `name, username, age, email, password, gender` as inputs
- Login to the application by providing existing `email, password` as inputs
- Creating a new task and adding it to a todo list
- Viewing todo list tasks with `pending`, `done` and `completion` percentage details
- Deleting an existing task from the todo list
- Editing a specific task from the todo list
- Deleting all tasks from the todo list
##### Technologies used
- HTML5/CSS
- Python 3
- TDD - Test Driven Development using the [unittest](https://docs.python.org/3/library/unittest.html) python library.
- Flask
#### Resources:
- HTML/CSS - [Link 1](https://www.tutorialspoint.com/html/), [Link 2](https://www.tutorialspoint.com/css/)
- Python 3 - [Link 1](https://www.tutorialspoint.com/python3/), [Link 2](https://docs.python.org/3.6/tutorial/index.html).
- OOP - [Link 1](https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3), [Link 2](https://www.digitalocean.com/community/tutorial_series/object-oriented-programming-in-python-3)
- TDD - [Link 1](https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137), [Link 2](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/UnitTesting.html), [Link 3](https://www.udemy.com/unit-testing-and-tdd-in-python/).
- Flask - [Link 1](http://flask.pocoo.org/docs/1.0/)
- Flask Restful - [Link 1](https://flask-restful.readthedocs.io/en/latest/)
