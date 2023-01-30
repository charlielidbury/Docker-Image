FROM ubuntu:22.04
RUN apt-get update -y
RUN apt-get install curl wget git build-essential openjdk-11-jdk-headless openssh-server sudo cmake maven -y
CMD /usr/bin/bash
