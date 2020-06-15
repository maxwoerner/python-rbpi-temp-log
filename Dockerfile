FROM python:3-alpine

WORKDIR /app

COPY run.py ./

RUN pip install 'gpiozero==1.5.1'

CMD [ "python3", "./run.py" ]