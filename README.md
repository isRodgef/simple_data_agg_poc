# simple_data_agg_poc

to run this all that is needed is docker and docker-compose 

docker-compose up -d 
#builds and runs the gunicorn server and the mongodb docker container

how it works 

the endpoint sendPatientData gets json data in a post request it gets validated and then sent into the mongodb database

improvements use an .env to manage running ports and connections for server and db
move all code into a better folder sturcture 
improve the repository pattern for the db connection