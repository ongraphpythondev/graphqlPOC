# GraphQL_CRUD_Application

<p> Quizze POC</p>

## Prerequisites:
You will need the following programmes properly installed on your computer.
    
```bash
Python 3.6+
Virtual Environment
```

To install virtual environment on your system use:

```bash
pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)
```

## Installation

```bash
git clone https://github.com/ongraphpythondev/graphqlPOC.git

cd graphqlPOC


virtualenv venv
      or
virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# install required packages for the project to run
pip install -r requirments.txt

```

## Running:

```bash
# activate the virtual environment
venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux


# run server
1.python manage.py makemigrations
2.python manage.py migrate
3.python manage.py createsuperuser
    username:
    email:
    password:
    conform_password:
5.python manage.py runserver
```
## Url
http://127.0.0.1:8000/admin <br>
http://127.0.0.1:8000/graphql

## Use graphiQL
# Get Operation
# user Details
```bash
query{
  users{
    id,
    username,
    email,
    password
  }
# User by id
query{
  users(id:id_value){
    id
    username
  }
``` 
# Get all Quizze Details
```bash
query{
  allQuizzes{
  	id
    title
    category {
      id
      name
    }
  }
  allAnswer{
    question{
      title
    }
  }
}
its return Quizze list with category and answer list question
```
# Create user
```bash
#Put Field value and execute
mutation{
  createUser(username:"username",password:"password"){
    ok
  } 
}
```
# Update User
```bash
#update by id with field value
mutation{
  updateUser(id:id_value,updated Field list value){
    ok
  } 
}
```
# Delete User
```bash
#delete user by id
mutation{
  deleteUser(id:id_value){
    ok
  } 
}
```

