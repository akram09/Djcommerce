FROM python:3.8.0-alpine


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN mkdir /Djcommerce
WORKDIR /Djcommerce

COPY requirements.txt /Djcommerce/

RUN pip install -r requirements.txt

COPY . /Djcommerce/
RUN rm -rf /Djcommerce/env/
