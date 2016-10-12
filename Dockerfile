########################################################
# Dockerfile to install python APYS framework
# and start a server
# Based on oficial python Dockerfile
########################################################
FROM python:3-alpine

MAINTAINER Rodrigo Seiji Piubeli Hirao <rodrigo.seiji.hirao@gmail.com>

# log
RUN mkdir -p /var/log/apys

RUN mkdir -p /usr/src/app/back
WORKDIR /usr/src/app/back

COPY . /usr/src/app/back/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["apys", "-s", "--config=dev.json"]

EXPOSE 8888