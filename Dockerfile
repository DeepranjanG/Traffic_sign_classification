FROM python:3.7.5-slim

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    apt-get install -y build-essential cmake && \
    apt-get install -y libopenblas-dev liblapack-dev && \
    apt-get install -y libx11-dev libgtk-3-dev
    
COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "clientApp.py" ]
