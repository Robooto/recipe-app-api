# Notes

## Docker Stuff

Copy the requirements, install the requirements
Creak the directory, copy the code
Create a user and use that user

docker build . - builds the image

## Docker Compose
Set up multiple docker services

docker-compose run app <command to run>

docker-compose run app sh -c ""  - run command on python server

example docker-compose run app sh -c "django-admin.py startproject app ."