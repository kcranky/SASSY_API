# SASSY_API
An API for the Student Attendance and Submission System.

## Requirements
The following is required for development:  
  - Ubuntu
  - PostGres
  - Python 3
  - PyCharm (Professional version recommended - Obtainable through the Github student pack)
  
## Installation
Installation takes place in a few steps. 

1) First, install Pycharm   
```$ snap install pycharm-professional```  
2) Configure Postgres. Items in <> brackets are variables
```
$ sudo su - postgres  
$ psql
$ CREATE DATABASE sassy;
$ CREATE USER <username> WITH PASSWORD '<password>';
$ ALTER ROLE <username> SET client_encoding TO 'utf8';
$ ALTER ROLE <username> SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE <username> SET timezone TO 'UTC+2';
$ GRANT ALL PRIVILEGES ON DATABASE sassy TO <username>;
$ \q
$ exit
$ sudo /etc/init.d/postgresql restart
```
3) Pull the repository:  
    Open PyCharm and select "open from repository". Enter the following URL: ```https://github.com/kcranky/SASSY_API```
    Pycharm will take a while to index the project.

4) Set Up Pycharm
    - Open Pycharm   
    - Select File - Open and open the seat directory (~/PycharmProjects/SASSY_API)
    - Navigate to File - Settings
    - Under "Project: seat" - "Project Interpreter", ensure that the project interpreter is set to \verb| ~/PycharmProjects/SASSY_API/venv/bin/python|
    - Close and reopen PyCharm to complete the loading
  
5) Setting Configurations
    - Import ```settings.py``` to /SASSY_API/Sassy
    - In ```settings.py```, adjust the username and password for database access
    - Run ```$ python manage.py makemigrations```
    - Run ```$ python manage.py migrate```
    - Run ```$ python manage.py makemigrations sassy_api```
    - Run ```$ python manage.py migrate```
    
6) Create a superuser
    - Run ```python manage.py createsuperuser``` and follow the prompts. You do not need to use a legitimate email address.
    
7) Run the server   
   You can run a local development server by using ```$ python manage.py runserver```. Navigate to ```127.0.0.1:8000/api/``` in your browser to see the server running.