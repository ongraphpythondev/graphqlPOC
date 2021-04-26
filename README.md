# GraphQL_CRUD_Application

<p> In this POC user can perform crud operations</p>

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
python manage.py migrate
```

## Running:

```bash
# activate the virtual environment
venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# run server
python manage.py runserver
```




