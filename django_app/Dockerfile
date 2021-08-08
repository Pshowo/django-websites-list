FROM python:3.8

COPY . .
RUN . /env/bin/activate && pip install -r requirements.txt
RUN . /env/bin/activate && python3 manage.py migrate

CMD . /env/bin/activate && gunicorn --bind 0.0.0.0:8080 website.wsgi