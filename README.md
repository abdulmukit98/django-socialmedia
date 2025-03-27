## Django Socialmedia

Hello Django Lovers. This is a social media application made with django.<br><br>
Source code documentation live at
https://abdulmukit98.github.io/django-socialmedia/

## Run Locally
Install required package through this command
```
pip install -r requirements.txt
```

To run the application
```
python manage.py runserver
```

### Docker run guide
```
docker-compose down
docker-compose up --build
```

### Docker VS .venv

* Running server locally need in **settings.py**
```
'HOST': localhost,
```

* But in using docker it is 
```
'HOST' : db, 
// db is the postgres service name in docker-compose.yml file
```

