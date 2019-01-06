# Notes

## Docker Stuff

Copy the requirements, install the requirements
Creak the directory, copy the code
Create a user and use that user

docker build . - builds the image

## Docker Compose and django commands
Set up multiple docker services

docker-compose build - builds docker image

docker-compose run app <command to run>

docker-compose run app sh -c ""  - run command on python server

example docker-compose run app sh -c "django-admin.py startproject app ."

Example - adding app to django - docker-compose run app sh -c "python manage.py startapp core"
    - docker-compose run --rm app sh -c "python manage.py startapp user"

Example running tests - docker-compose run app sh -c "python manage.py test && flake8"

RUN apk add --update --no-cache postgresql-client
    - installs postgresql-client on our python package

Manager command to wait for db
## Travis Ci


## Mocking
patch - allows you to overwrite a function and set it's output
It can also be used as a decorator
Example

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # returns operations error 5 times then returns true
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)

## Random
Need to restart docker for windows occationally to deal with odd issues

## Runing commands on instance
docker-compose run --rm app sh -c "python manage.py createsuperuser"
 - --rm removes container after command is completed

## ORM stuff
Need to run migrations after creating a new model
Then register in the admin site

Don't make char fields null make them blank