## Content
This project is built on images of ubuntu, nginx, postgres <br/>
Frontend is implemented by using simple React components. <br/>
Project settings are located in the `server` directory <br/>
Application in the `todo` directory <br/>

## Launch of the project 
Clone the project. In the root directory of the project, execute the command
`docker-compose up` (to start in detached mode use `docker-compose up -d`). 
This will start the containers build process and execution 
of `entrypoint.sh` file which provides migration to the database and the start of the webapp server. 
After the build is complete and the server has started, go to `127.0.0.1:8000` <br/>
To access the admin panel, you need to execute the command
`python3 manage.py createsuperuser` in the cli of the container in Docker Desktop or via
`docker exec -ti my_container sh c "python3 manage.py createsuperuser"`

##### Git
If you are using Windows OS, before downloading, make sure that
`git config --global core.autocrlf false` otherwise there may be incorrect 
endings in the `entrypoint.sh` file (CRLF instead of LF)

## Restart container
`docker-compose restart` After making changes in the project, 
this command will reload container

## Remove container
`docker-compose down` 

## API:
implemented with DRF. <br/>
API ROOT: `/api/`

##### GET
`/api/todo/` list of todo tasks <br/>
`/api/todo/<int:pk>/` details of certain todo <br/>

##### POST
`/api/todo/` create new todo <br/>

##### PUT
`/api/todo/<int:pk>/` update todo

##### DELETE
`/api/todo/<int:pk>/` delete todo

## Learn More

You can learn more in the [Django documentation](https://docs.djangoproject.com/en/3.1/).

To learn DRF, check out the [Django Rest Framework documentation](https://www.django-rest-framework.org/).

Deploy Django application on [Heroku Devcenter](https://devcenter.heroku.com/categories/python-support) 


#### `.env` file :
	SECRET_KEY = "Your Data goes herer"
	DB_NAME = "Your Data goes herer"
	DB_USER = "Your Data goes herer"
	DB_PASSWORD = "Your Data goes herer"
	DB_HOST = "Your Data goes herer"
	DB_PORT = "Your Data goes herer"
	
	REDIS_LOCATION = "Your Data goes herer"
	


