FROM python:3.7-slim
RUN mkdir /fampay
WORKDIR /fampay
ADD . /fampay
RUN pip install -r requirements.txt
CMD python manage.py makemigrations
CMD python manage.py migrate
EXPOSE 8000
CMD python manage.py runserver 0:8000
