########################################################
# Dockerfile to build Polymer project and move to server
# Based on oficial nginx Dockerfile
########################################################
FROM python:2.7

MAINTAINER Rodrigo Seiji Piubeli Hirao <rodrigo.seiji.hirao@gmail.com>

RUN mkdir -p /usr/src/app/dev
WORKDIR /usr/src/app/dev

COPY . /usr/src/app/dev/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pypolyback", "-s"]