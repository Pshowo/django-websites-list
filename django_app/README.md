# django-websites-list


## Uruchomienie aplikacji
1. `sudo docker-compose up --build`
2. `sudo docker-compose exec dj_app python manage.py migrate`
3. `sudo docker-compose exec dj_app python manage.py shell`

        >> from app.tasks import load_data
        >> load_data()
        >> exit()


> Web application with websites list.

## Requirements:

* Django
* Baza Postgres SQL 
* Celery, Rabbitmq

### Models:

* Website:
     - url
     - title
     - meta_description
     - alexa_rank (__int__)
     - category FK Website Category
     - date_added DT
     - date_updated DT

* Website Category
    - name
    - description
    - date_added
    - date_updated
    - count - int

* WebPage:
     - website FK Website
     - URL - unikalny
     - date_added
     - date_updated
     - title
     - meta description

### Views:

* List view - widok listy wpisw w modelu website:
    - filtrowanie po kategorii
    - sortowanie po kolumanch
    - paginacja 25

* Detail view dla Website
    - wszystkie dane

### Celery task:

* Pobranie pliku csv [alexa](http://s3.amazonaws.com/alexa-static/top-1m.csv.zip).
* Ponowne pobranie aktualizuje wpisy
