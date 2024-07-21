FROM python:3.10-alpine3.19
WORKDIR /usr/src/app

COPY . .

CMD [ "python", "main.py" ]


