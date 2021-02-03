FROM python:3.7.9

WORKDIR /appboxo

COPY ./requirements.txt /requirements.txt
COPY ./entrypoint.sh /entrypoint.sh

RUN pip3 install -r /requirements.txt

COPY . .

ENTRYPOINT ["sh","/entrypoint.sh"]