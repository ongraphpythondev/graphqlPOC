# GraphQL_CRUD_Application

<p> Features of this POC is
<br>
1.Implementation of GraphQL<br>
2.Authentication of User with JWT token<br>
3.Its Contain information like Quizze Application</p>

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
# activate the virtual environment and run the server

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
By using above url we can login and Perform operation with admin panel.<br>
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
Its return Quizze list with category and answer list question.
```
# Register user
```bash
#Put Field value and execute
mutation{
  register(email:"email",username:"username",password1:"password",password2:"password"){
    success,
    errors,
    token,    
    refreshToken
  } 
}
Its return true success,token,refreshtoken of register user.
```
# Verify Account of User
```bash
#Verify Account of user by valid token
mutation{
  verifyAccount(token: "token value"){
    success
    errors
  }
}
Its return Sucees=True otherwise Error if token value not valid.
```
# Get User Details Based on username and password
```bash
#update Details of login user
mutation{
  tokenAuth(username:"username",password:"password"){
    success
    errors
    token
    refreshToken
    user{
      username
    }
  }
}
Its return of sucess,token,refreshtoken along with user details.
```
# Update User
```bash
#update Details of login user
mutation{
  updateAccount(fieldname:"value"){
    success
    errors
  }
}
Its return sucess=True otherwise throw error in case of details is not valid.
```


