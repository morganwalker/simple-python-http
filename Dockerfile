# gunicorn-flask
FROM ubuntu:14.04
MAINTAINER Morgan Walker <j.morganwalker@gmail.com>

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Define build variables for port exposure. Bind to port if defined during build, otherwise default to:
ARG PORT=8000

# Define run variables for port and workers. Set port and workers if defined during run, otherwise default to:
ENV WORKERS=2
ENV PORT=8000

RUN apt-get update
RUN apt-get install -y python python-pip python-virtualenv gunicorn

# Setup flask application
RUN mkdir -p /deploy/app
WORKDIR /deploy/app
COPY requirements.txt /deploy/app/requirements.txt
RUN pip install -r requirements.txt
COPY main.py /deploy/app/main.py
EXPOSE ${PORT}

# Start gunicorn
CMD gunicorn -w ${WORKERS} -b 0.0.0.0:${PORT} main:app