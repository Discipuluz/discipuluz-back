########################################################
# Dockerfile to build Polymer project and move to server
# Based on oficial nginx Dockerfile
########################################################
FROM python:2.7

MAINTAINER Rodrigo Seiji Piubeli Hirao <rodrigo.seiji.hirao@gmail.com>

RUN mkdir -p /usr/src/app/prod
WORKDIR /usr/src/app/prod

COPY ../ /usr/src/app/prod/

RUN pip install --no-cache-dir -r requirements.txt

ONBUILD RUN pypolyback -s