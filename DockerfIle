FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /djecommerce
WORKDIR /djecommerce
COPY requirements.txt /djecommerce/
RUN pip install -r requirements.txt
COPY . /djecommerce/
RUN rm -rf /djecommerce/env/
