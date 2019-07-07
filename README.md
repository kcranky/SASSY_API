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
Pull 