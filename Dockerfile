FROM python:3.7

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]