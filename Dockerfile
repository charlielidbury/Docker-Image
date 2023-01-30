FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install curl wget git build-essential cmake maven -y
RUN apt-get install openssh-server sudo -y
CMD /usr/bin/bash
