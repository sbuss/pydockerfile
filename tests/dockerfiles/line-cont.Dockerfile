FROM ubuntu
RUN apt-get update && \
    apt-get install -y \
        python \
        python-pip
CMD bash
