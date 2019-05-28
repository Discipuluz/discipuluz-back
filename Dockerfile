########################################################
# Dockerfile to install python APYS framework
# and start a server
# Based on oficial python Dockerfile
########################################################
FROM python:3-alpine

MAINTAINER Rodrigo Seiji Piubeli Hirao <rodrigo.seiji.hirao@gmail.com>

ENV CONFIG prod

# -- Configure environment
RUN mkdir -p /var/log/apys

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/

COPY . /usr/src/app/

# -- Install pipenv
RUN pip install --upgrade --no-cache-dir pipenv

# -- Install dependencies:
ONBUILD RUN set -ex && pipenv install --deploy --system

# -- Run apys
CMD apys -s --config=$CONFIG

EXPOSE 8888
