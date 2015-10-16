FROM ubuntu:trusty

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip

CMD bash
