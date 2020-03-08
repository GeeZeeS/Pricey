# PriceyBackup

# Installation:
### Docker:
###### build a docker image
```
> docker-compose build
```
###### run a docker container
###### silent (no debug)
```
> docker-compose up -d
```
###### debug mode
```
> docker-compose up
```
###### Populate db
```
> docker-compose exec web python manage.py migrate
```