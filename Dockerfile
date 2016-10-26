########################################################
# Dockerfile to install python APYS framework
# and start a server
# Based on oficial python Dockerfile
########################################################
FROM python:3-alpine

MAINTAINER Rodrigo Seiji Piubeli Hirao <rodrigo.seiji.hirao@gmail.com>

ENV CONFIG prod

# log
RUN mkdir -p /var/log/apys

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["apys", "-s", "--config=$CONFIG"]

EXPOSE 8888