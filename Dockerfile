FROM python:3-alpine

WORKDIR /app

COPY run.py ./

RUN pip install gpiozero

CMD [ "python3", "./run.py" ]