# Introduction
Building a Django backend for a blog that presents GraphQL connectivity. Original code created whilst learning from https://realpython.com/python-django-blog/ , and then built upon.

Frontend is built in Vue and available at: https://github.com/geektechdude/blog-vue-frontend

# Installation
- Clone the repository
- Open the repository (change to the repository directory)
- Create a Virtual Environment using the command "python3 -m venv ./venv"
- Activate the Virtual Environment using the command "source ./venv/bin/activate"
- Install the required Python modules using the command "pip install -r requirements.txt"
- Run Django server using command "python manage.py runserver"

# Environment Variables
The app uses enviroment variables, it is recommended not to leave the defaults in place.

- DJANGO_SECRET_KEY
A secure secret key should be used
- DJANGO_DEBUG
Expects a TRUE or FALSE value. TRUE runs in debug mode and should not be used in production
- DJANGO_DB_ENGINE
Which database engine should be used
- DJANGO_DB_NAME
Name of the database to connect to
- DJANGO_DB_USER
Name of the database user to connect with
- DJANGO_DB_PASS
Password for the database user
- DJANGO_DB_HOST
Host where the database is running
- DJANGO_DB_PORT
Port on the host where the database is running
