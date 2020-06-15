FROM python:3-alpine

WORKDIR /app

COPY run.py ./

CMD [ "python3", "./run.py" ]