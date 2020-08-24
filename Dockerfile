FROM python:3.8.5

WORKDIR /app
COPY app/ /app/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN apt-get update -y && apt-get install -y libopencv-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

CMD cd src && gunicorn server:app -c config/gunicorn_conf.py
