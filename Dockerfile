FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./requirements.txt /app
COPY ./data.json /app
ADD ./cars /app/cars
ADD ./templates /app/templates
ADD ./vehicles /app/vehicles
ADD ./static /app/static
ADD ./manage.py /app
RUN pip install -r requirements.txt
CMD python manage.py migrate \
    && gunicorn -b 0.0.0.0:8000 vehicles.wsgi
