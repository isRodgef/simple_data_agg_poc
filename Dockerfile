FROM python:3.6.8-alpine

WORKDIR /home/app

COPY app.py .
COPY mongoRepository.py .
COPY repository.py .

COPY requirements.txt /tmp/


RUN pip install --upgrade pip
RUN pip install cython
RUN apk add libffi-dev
RUN python3 -m pip install -r /tmp/requirements.txt

EXPOSE 8000
CMD gunicorn app:app --bind 0.0.0.0