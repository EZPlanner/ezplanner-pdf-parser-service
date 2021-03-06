FROM python:3.7.1-slim

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]