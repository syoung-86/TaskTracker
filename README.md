# TaskTracker

## Setup

1. Run setup.sh 
- this script setups a python virtual enviroment, installs pip and node depenencies, creates 2 users then runs the django server.  
2. navigate to `http://127.0.0.1:8000/` and login with one of the users below.


**superuser:** username: `admin` password: `plain-password`  
**user:** username: `testuser` password: `plain-password`  

Alternativley run the following commands:
```sh 
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

npm install

python manage.py migrate

python manage.py create_default_users

python manage.py runserver
```
