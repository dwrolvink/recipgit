FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade

RUN mkdir /app
WORKDIR /app
COPY app/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python", "app.py" ]