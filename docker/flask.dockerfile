FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update --fix-missing > /dev/null 2>& 1; \
    apt-get install -y \
    build-essential bzip2 \
    ca-certificates cmake curl \
    libpq-dev \
    git \
    python3 python3-pip \
    wget;

RUN pip3 install -r /app/requirements.txt