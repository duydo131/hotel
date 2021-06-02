FROM python:3
RUN pip install --upgrade pip
WORKDIR ./

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate; python manage.py runserver 0.0.0.0:8000; celery -A config worker -B -l info -c 3;"]