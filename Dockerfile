FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /apistoom
WORKDIR /apistoom
COPY requirements.txt /apistoom/
RUN pip install -r requirements.txt
COPY . /apistoom/
