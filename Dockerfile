#FROM python:3.7.9
FROM ubuntu:18.04 as base

WORKDIR /appboxo

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Install Ubuntu dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        libopencv-dev \
        build-essential \
        libssl-dev \
        libpq-dev \
        libcurl4-gnutls-dev \
        libexpat1-dev \
        gettext \
        unzip \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        gunicorn \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /requirements.txt
COPY ./entrypoint.sh /entrypoint.sh

RUN pip3 install -r /requirements.txt

COPY . .

ENTRYPOINT ["sh","/entrypoint.sh"]