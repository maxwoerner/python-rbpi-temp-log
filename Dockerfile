FROM python:3-alpine

WORKDIR /app

COPY run.py ./

RUN pip3 install gpiozero

CMD [ "python3", "./run.py" ]
