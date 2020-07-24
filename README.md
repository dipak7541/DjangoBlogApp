# DjangoBlogApp


This implement this project first create virtual environment using following commnads
  virtualenv virtualenvironmentname
  source virtualenvironmentname/bin/activate

Then install django using pip installer inside this virtual environment.

This project is implemented using postgresql if you want to use default django database sqlite3, you can alter the setting.py with following lines:
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.database',
        'NAME': 'your database name',
        }
    }
    
  Database name will be databases like sqlite3, postgresql,mongoDb etc
  and Your Database name will be the name of database name specified for this project
  
Here custom user model is implemented so make sure to add:
AUTH_USER_MODEL="blogs.AutherRegistration'

make sure to add static and media files in setting.py 
